from collections import defaultdict

def readLinesFromFile(filename):
    lines = []
    for line in open(filename, 'r'):
        splittedLine = line.split()
        # index 1 is always a step requirments and index 7 a step for which requirement is listed
        lines.append((splittedLine[1], splittedLine[7]))
    return lines

def getNextStep(stepsRequirementsGraph, leftToDoSteps, stepsAlreadyDone):
    # print(stepsRequirementsGraph)
    # print(leftToDoSteps)
    # print(stepsAlreadyDone)
    currentlyAvailableSteps = []
    for singleStepLeftToResolve in leftToDoSteps:
        requiredSteps = stepsRequirementsGraph[singleStepLeftToResolve]
        if len(requiredSteps) == 0 or  stepsAlreadyDone >= set(requiredSteps):
            currentlyAvailableSteps.append(singleStepLeftToResolve)
    # sort
    # print(currentlyAvailableSteps)
    currentlyAvailableSteps.sort()
    # return first element
    return currentlyAvailableSteps[0]

def main():
    # This will contain answer for part 1
    orderOfSteps = []

    # It will contain all available steps characters, we will remove elemets from that as soon as step can be completed
    # Alogrithm should stop when this set is empty
    uniqueSteps = set()

    # It will contain each step name and required steps in order to complete that
    stepsRequirements = defaultdict()

    # Steps already processed
    stepsAlreadyProcessed = set()

    # Load the steps description
    steps = readLinesFromFile('input.txt')
    
    # Let's process the steps first
    for (stepRequirement, step) in steps:
        # Add everything to set
        uniqueSteps.add(stepRequirement)
        uniqueSteps.add(step)
        # Add requirement for step
        stepsRequirements.setdefault(step, []).append(stepRequirement)
    # A basic map graph like is created
    # Let's find all steps that do not require any other steps to be completed
    for uniqueStep in uniqueSteps:
        if stepsRequirements.get(uniqueStep) is None:
            # Add also them to stepsRequirements with empty requirements
            stepsRequirements[uniqueStep] = []

    # Loop until uniqueSteps is not empty, we will graduately remove elements from that set as we resolve more steps
    while len(uniqueSteps) != 0:
        nextStep = getNextStep(stepsRequirements, uniqueSteps, stepsAlreadyProcessed)
        orderOfSteps.append(nextStep)
        uniqueSteps.remove(nextStep)
        stepsAlreadyProcessed.add(nextStep)

    # Part 1
    print(''.join(orderOfSteps))    


main()