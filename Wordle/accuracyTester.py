from Testing import getColorList, chooseGuessWithBestEntropyPlusFreq

with open("FiveLetterWords2.txt") as f:
    allGuesses = f.read().splitlines()

with open("WordleAnswersList.txt") as f:
    allAnswers = f.read().splitlines()

def find_possible_words(word, colorList, initialPossibilities):
    possibleWords = initialPossibilities
    for i in range(len(colorList)):
        if colorList[i] == "G":
            possibleWords = [oneWord for oneWord in possibleWords if oneWord[i] == word[i]]
        elif colorList[i] == "B":
            possibleWords = [oneWord for oneWord in possibleWords if word[i] not in oneWord]
        else:
            possibleWords = [oneWord for oneWord in possibleWords if word[i] in oneWord and oneWord[i] != word[i]]
    return possibleWords


def playForAns():
    initialPossibilities = allGuesses.copy()
    iterationNo = 1
    bestAns = "raise"
    while iterationNo <= 6:
        print(bestAns, ans)
        # bestAns = chooseGuessWithBestEntropyPlusFreq(initialPossibilities)
        # print(bestAns, ans)
        colorScrapedList = getColorList(bestAns.strip(), ans.strip())
        if colorScrapedList == "GGGGG":
            print(iterationNo)
            return iterationNo
        initialPossibilities = find_possible_words(bestAns.strip(), colorScrapedList, initialPossibilities)
        bestAns = chooseGuessWithBestEntropyPlusFreq(initialPossibilities)
        iterationNo += 1
    return -1


avg = 0
noOfFailures = 0
count = 0
for ans in allAnswers:
    val = playForAns()
    if val != -1:
        avg += val
    else:
        noOfFailures += 1
    count += 1
    print(f"{(count*100)/len(allAnswers)}% complete")

totalGames = len(allAnswers)
avg = avg/(totalGames - noOfFailures)
accuracy = (totalGames - noOfFailures)/totalGames

print(f"Average no of guesses: {avg}")
print(f"No of failures: {noOfFailures}")
print(f"Accuracy: {accuracy}")

