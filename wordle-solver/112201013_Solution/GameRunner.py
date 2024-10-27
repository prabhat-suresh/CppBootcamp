'''
    Author: Bhogaraju Shanmukha Sri Krishna
    Roll No: 112201013

    Contains the main code for running the game. 
    This takes the entire list of words and filters it according to user inputs
'''


import random

def run(maxChances, allWords):
    found = False
    for _ in range(maxChances):

        '''
            Firstly check if the resulted word list is non empty because if this is empty, 
            the next step will create an error
        '''
        if not allWords:
            print("Sorry I don't know such a word exists :(")
            break
        
        # Choosing a random word from all the words
        currWord = random.choice(allWords)

        # Prompting the user to enter this in the game
        print("Enter the following word and check\n%s" % currWord)

        # Game might be done just after answer is entered
        temp = input('Is your game done? (y/n) ')
        if temp == 'y':
            found = True
            # If the game is done, prompt a message and break   
            print("Congratulations on winning the game :)")
            break

        '''
            Check if there is any green letter. Because green letters are the most precious to 
            reduce the search space and proceed accordingly
        ''' 
        temp = input('Is there any letter with green color? (y/n) ')
        isGreenPresent = True if temp == 'y' else False

        yellowLetters = []
        greenLetters = []
        if isGreenPresent:
            # Ask the user to prompt a sequence of indices because we have the letters with us in the word 
            # earlier
            greenIndices = list(map(int, input('Give space seperated indices (0 based)\n').split()))
            greenLetters = [currWord[i] for i in greenIndices]


            # Collection of all words with a specific in it at the exact index

            for ind in greenIndices:
                changedSpace = []
                # Get the current letter. Can be avoided but used for good readability
                currLetter = currWord[ind] 

                for word in allWords:
                    '''
                        Index traversal. We only need those words whose element at the given index is 
                        matching since it is green colored
                    '''
                    if word[ind] == currLetter:
                        changedSpace.append(word)

                allWords = changedSpace
                

        # Ask for yellow colored letters
        temp = input('Is there any letter with yellow color? (y/n) ')
        isYellowPresent = True if temp == 'y' else False
        if isYellowPresent:
            yellowLetters = input('Give space seperated letters\n').split()
            
            # Similar filtering as above but we only need the words which contains all the yellow letters
            for letter in yellowLetters:
                changedSpace = []
                for word in allWords:
                    if letter in word:
                        changedSpace.append(word)
                allWords = changedSpace
                

        # Taking all letters which are either yellow or green
        greenPlusYellow = greenLetters + yellowLetters

        # All remaining letters in the word are gray
        grayLetters = []
        for letter in currWord:
            if letter not in greenPlusYellow:
                grayLetters.append(letter)

        for letter in grayLetters:
            changedSpace = []

            # Filtering: Leave out all the words which contain gray letters
            for word in allWords:
                if letter not in word:
                    changedSpace.append(word)

            allWords = changedSpace
    if not found:
        print("Sorry that I could not help you. I don't know such a word exists :(")