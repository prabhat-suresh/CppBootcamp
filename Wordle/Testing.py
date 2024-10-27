import math

with open("FiveLetterWords2.txt") as f:
    allGuesses = f.readlines()

with open("WordleAnswersList.txt") as f:
    allAnswers = f.readlines()


def getColorList(guess, ans):
    colorList = ""
    for i in range(5):
        if guess[i] == ans[i]:
            colorList += "G"
        elif guess[i] in ans:
            colorList += "Y"
        else:
            colorList += "B"
    return colorList


def getEntropy(guess):
    colorListsEnumerated = {}
    for ans in allAnswers:
        colorList = getColorList(guess, ans)
        colorListsEnumerated[colorList] = colorListsEnumerated.get(colorList, 0) + 1
    totalAnswers = len(allAnswers)
    entropy = 0
    for colorList in colorListsEnumerated.keys():
        noOfPossiblities = colorListsEnumerated[colorList]
        probability = noOfPossiblities / totalAnswers
        entropy -= probability * math.log2(probability)
    return entropy


def chooseGuessWithBestEntropy(reducedPossibilities):
    maxEntropy = 0
    chosenGuess = ""
    for guess in reducedPossibilities:
        entropy = getEntropy(guess)
        if entropy > maxEntropy:
            maxEntropy = entropy
            chosenGuess = guess
    return chosenGuess

