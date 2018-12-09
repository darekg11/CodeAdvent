from collections import defaultdict

def readLinesFromFile(filename):
    lines = []
    for line in open(filename, 'r'):
        splittedLine = line.split()
        # index 1 is always a step requirments and index 7 a step for which requirement is listed
        lines.append((splittedLine[1], splittedLine[7]))
    return lines

def getNextSteps(stepsRequirementsGraph, leftToDoSteps, stepsAlreadyDone):
    currentlyAvailableSteps = []
    for singleStepLeftToResolve in leftToDoSteps:
        requiredSteps = stepsRequirementsGraph[singleStepLeftToResolve]
        if len(requiredSteps) == 0 or  stepsAlreadyDone >= set(requiredSteps):
            currentlyAvailableSteps.append(singleStepLeftToResolve)
    # sort
    currentlyAvailableSteps.sort()
    # return first element
    return currentlyAvailableSteps

def getNextStep(stepsRequirementsGraph, leftToDoSteps, stepsAlreadyDone):
    return getNextSteps(stepsRequirementsGraph, leftToDoSteps, stepsAlreadyDone)[0]

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

    # Part 2 - wtf the workers
    orderOfSteps = []
    uniqueSteps.clear()
    stepsAlreadyProcessed.clear()

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

    totalTime = 0
    # First index is current job, the second is time requirement and the third is time spent on task
    workers = [['', 0, 0], ['', 0, 0], ['', 0, 0], ['', 0, 0], ['', 0, 0]]
    
    # Loop until uniqueSteps is not empty and all workers are done
    while len(uniqueSteps) != 0 or len([worker for worker in workers if worker[0] == '']) != len(workers):
        avilableTasksForWorkers = getNextSteps(stepsRequirements, uniqueSteps, stepsAlreadyProcessed)
        availableWorkers = [worker for worker in workers if worker[0] == '']
        for workerCnt in range(len(availableWorkers)):
            # there can be more workers than task so always check if we are not outside of index ranges
            if workerCnt < len(avilableTasksForWorkers):
                taskLetter = avilableTasksForWorkers[workerCnt]
                availableWorkers[workerCnt][0] = taskLetter
                # always do - ord('A') to get bottom value + 1 becasue ord('A') - ord('A') would be 0 and 60 is a time defined for a task
                availableWorkers[workerCnt][1] = ord(taskLetter) - ord('A') + 1 + 60
                uniqueSteps.remove(taskLetter)
        totalTime += 1
        for worker in workers:
            # if worker has a task
            if worker[0] != '':
                # update how much that worker spent time
                worker[2] += 1
                # if task requirement is equal to time that worker has spent on it
                if worker[1] == worker[2]:
                    # add to steps that are done
                    stepsAlreadyProcessed.add(worker[0])
                    # mark worker as free
                    worker[0] = ''
                    # clear timers
                    worker[1] = 0
                    worker[2] = 0
    print(totalTime)
main()