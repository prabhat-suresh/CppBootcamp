import math
from wordfreq import word_frequency

with open("FiveLetterWords2.txt") as f:
    allGuesses = f.read().splitlines()

with open("WordleAnswersList.txt") as f:
    allAnswers = f.read().splitlines()

possibilitiesFreq = [(word.strip(), word_frequency(word.strip(), 'en')) for word in allGuesses]
possibilitiesSorted = sorted(possibilitiesFreq, key=lambda x: x[1], reverse=True)
# print(possibilitiesSorted)
possibilitiesSorted = [(word,1) for (word,freq) in possibilitiesSorted if possibilitiesSorted.index((word,freq)) < len(possibilitiesSorted)/2] + [(word,0) for (word,freq) in possibilitiesSorted if possibilitiesSorted.index((word, freq)) >= len(possibilitiesSorted)/2]
possibilitiesSortedDict = dict(possibilitiesSorted)


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


def getFreq(guess):
    return possibilitiesSortedDict[guess]

def chooseGuessWithBestEntropyPlusFreq(reducedPossibilities):
    maxVal = 0
    chosenGuess = ""
    for guess in reducedPossibilities:
        entropy = getEntropy(guess)
        freq = getFreq(guess)
        totalVal = entropy + freq
        if totalVal > maxVal:
            maxVal = totalVal
            chosenGuess = guess
    return chosenGuess

