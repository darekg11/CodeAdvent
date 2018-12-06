from collections import deque

def readLinesFromFile(filename):
    inputFile = open(filename, 'r')
    lines = inputFile.read()
    inputFile.close()
    return lines

def reactPolimer(polimer):
    # This is a queue from input string 
    # We will iterate throught it and place input correctly on output queue
    inputPolimerQueue = deque(polimer)
    # This is our output queue containing final polimer
    outputPolimerQueue = deque()
    for elem in inputPolimerQueue:
        if len(outputPolimerQueue) == 0:
            outputPolimerQueue.append(elem)
        else:
            # Get the newest chemcial structure in output queue
            currentTopElementInOutputQueue = outputPolimerQueue[-1]
            # Compare with current chemical structure from input queue to see if those two react with each other
            ascii_difference = abs(ord(currentTopElementInOutputQueue) - ord(elem))
            # 32 is integer difference between uppercase and lowercase of the same letter
            # if that happens, that means we need to pop element from output queue as those two reacted with each other
            if ascii_difference == 32:
                outputPolimerQueue.pop()
            else:
                outputPolimerQueue.append(elem)
    return ''.join(outputPolimerQueue)
    

def main():
    polymerInput = readLinesFromFile('input.txt')
    outputPolimer = reactPolimer(polymerInput)
    # Part 1 - length of reacted polymer
    print(len(outputPolimer))

    # Part 2 - just iterate thrgouht the whole ascii alphabet and keep on removing and recalculating the shortest
    shortest = None
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for singleChar in alpha:
        improvedPolymer = polymerInput.replace(singleChar, '').replace(singleChar.upper(), '')
        reactedPolymer = reactPolimer(improvedPolymer)
        if shortest is None or len(reactedPolymer) < shortest:
            shortest = len(reactedPolymer)

    print(shortest)
    
main()
