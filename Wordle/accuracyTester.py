from Testing import getColorList, chooseGuessWithBestEntropy
from main import find_possible_words

with open("FiveLetterWords2.txt") as f:
    allGuesses = f.read().splitlines()

with open("WordleAnswersList.txt") as f:
    allAnswers = f.read().splitlines()


def playForAns():
    initialPossibilities = allGuesses.copy()
    iterationNo = 1
    bestAns = "soare"
    while iterationNo <= 6:
        print(bestAns, ans)
        colorScrapedList = getColorList(bestAns.strip(), ans.strip())
        if colorScrapedList == "GGGGG":
            print(iterationNo)
            return iterationNo
        initialPossibilities = find_possible_words(bestAns.strip(), colorScrapedList, initialPossibilities)
        bestAns = chooseGuessWithBestEntropy(initialPossibilities)
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

