import itertools

def readNumbersFromFileAndReturnThemInArray(filename):
    numbers = []
    with open(filename) as inputFile:
        for singleLine in inputFile:
            singleLine = singleLine.split()
            if (singleLine != ''):
                numbers.append(int(singleLine[0]))
    return numbers


def main():
    numbers = readNumbersFromFileAndReturnThemInArray('input.txt')
    frequencySet = set()
    firstDuplicatedFrequency = 0
    currentFrequency = 0
    totalSum = sum(numbers)
    for number in itertools.cycle(numbers):
        currentFrequency += number
        if (currentFrequency in frequencySet):
            firstDuplicatedFrequency = currentFrequency
            break
        frequencySet.add(currentFrequency)
    print(totalSum)
    print(firstDuplicatedFrequency)

main()