'''
    Author: Bhogaraju Shanmukha Sri Krishna
    Roll No: 112201013
    
    This file contains the snippet for obtaining the words from a file. This was used to take all the words
    from the WordleAnswersList.txt file
'''

def openFileAndGetWords(file):
    allPossibleAnswers = open(file)
    
    # In the Original files, all words end with a new line. 
    # So stripping the newline from words and using them 
    allWords = [i[:-1] for i in allPossibleAnswers]
    allPossibleAnswers.close()
    
    return allWords