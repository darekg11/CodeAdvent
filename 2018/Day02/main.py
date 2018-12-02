from collections import Counter

def readIdsFromFileAndReturnThemInArray(filename):
    inputFile = open(filename, 'r')
    lines = inputFile.readlines()
    inputFile.close()
    return lines

def countEveryCharacterInString(string):
    cnt = Counter(string)
    return cnt.values()

def differentByOneIndex(firstString, secondString):
    differencesCount = sum([firstString[i] != secondString[i] for i in range(len(firstString) - 1)])
    return differencesCount == 1

def main():
    ids = readIdsFromFileAndReturnThemInArray('input.txt')
    countOfTwoCharacters = 0
    countOfThreeCharacters = 0
    for singleId in ids:
        charactersCount = countEveryCharacterInString(singleId)
        if any(count == 2 for count in charactersCount):
            countOfTwoCharacters += 1
        if any(count == 3 for count in charactersCount):
            countOfThreeCharacters += 1
    checksum = countOfThreeCharacters * countOfTwoCharacters
    print(checksum)

    for singleId in ids:
        uniqueSet = set(ids)
        uniqueSet.discard(singleId)
        for singleIdToCompare in uniqueSet:
            if differentByOneIndex(singleId, singleIdToCompare):
                print(singleId)
                print(singleIdToCompare)

main()