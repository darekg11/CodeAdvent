from collections import defaultdict
import operator

def readLinesFromFile(filename):
    inputFile = open(filename, 'r')
    lines = inputFile.read().split('\n')
    lines.sort()
    return lines

def parseGuardLine(line):
    splitted = line.split()
    #3 is a piece starting with #123 ID
    return int(splitted[3][1:])

def parseReguarTimeLine(line):
    splitted = line.split()
    #1 is always time part of timestamp
    time = splitted[1]
    minutes = time.split(':')
    minutes_without_bracket = minutes[1][:-1]
    return int(minutes_without_bracket)

def main():
    guardsTotalTime = defaultdict(int)
    guardPerMinuteCounter = defaultdict(int)
    lines = readLinesFromFile('input.txt')
    currentGuard = None
    startTime = None
    endTime = None
    for line in lines:
        if "begins shift" in line:
            currentGuard = parseGuardLine(line)
            startTime = None
            endTime = None
        if "falls asleep" in line:
            startTime = parseReguarTimeLine(line)
        if "wakes up" in line:
            endTime = parseReguarTimeLine(line)
            for minute in range(startTime, endTime):
                # Update total sleep time of guard
                guardsTotalTime[currentGuard] += 1
                # Update counter of sleep occurences per minute per guard
                guardPerMinuteCounter[(currentGuard, minute)] += 1
    guardThatSleptTheMost = max(guardsTotalTime.items(), key=operator.itemgetter(1))[0]
    mostSleptMinute = None
    mostSleptMinuteCount = None
    for (guardId, minute), count in guardPerMinuteCounter.items():
        if guardId == guardThatSleptTheMost and (mostSleptMinuteCount is None or count > mostSleptMinuteCount):
            mostSleptMinute = minute
            mostSleptMinuteCount = count
    # part 1
    print(guardThatSleptTheMost * mostSleptMinute)

    # part 2 - go through every entry in created dict and find the most count per minute
    minuteFinal = None
    countFinal = None
    guardIdFinal = None
    for (guardId, minute), count in guardPerMinuteCounter.items():
        if (countFinal is None or count > countFinal):
            minuteFinal = minute
            countFinal = count
            guardIdFinal = guardId
    print(guardIdFinal * minuteFinal)
    
main()