def getInitialStateAndMutations(filename):
    inputFile = open(filename, 'r')
    lines = inputFile.readlines()
    inputFile.close()
    # get only those mutations that leads to plant being in pot
    # as we can default to emplty pot
    mutations = set()
    for mutation in lines[1:]:
        splitted = mutation.split()
        scheme = splitted[0]
        result = splitted[2]
        if result == '#':
            mutations.add(scheme)
    return lines[0].replace('\n', ''), mutations

def runMutation(currentState, mutationsToRun):
    min_index = min(currentState)
    max_index = max(currentState)
    indexes = set()
    # -10 and + 10 as safe guards to have enough big row
    for plant in range(min_index - 10, max_index + 10):
        scheme = []
        # -2 -1 0 1 2 becatuse two plants to the left and to to the righ
        for i in [-2, -1, 0, 1, 2]:
            if plant + i in currentState:
                scheme.append('#')
            else:
                scheme.append('.')
        scheme_as_string = ''.join(scheme)
        if scheme_as_string in mutationsToRun:
            indexes.add(plant)
    return indexes

def main():
    # Parse the input
    initialState, mutations = getInitialStateAndMutations('input.txt')
    # Find indexes where value is #
    indexes = set()
    for i in range(len(initialState)):
        if initialState[i] == '#':
            indexes.add(i)
    # Part 1 - Run 20 generations:
    for i in range(20):
        indexes = runMutation(indexes, mutations)
    print(sum(indexes))

    # Part 2 - Run fuck tons of generations - does not make sense. CPU would die.
    # Need to check if at some points generations are the same
    indexes = set()
    for i in range(len(initialState)):
        if initialState[i] == '#':
            indexes.add(i)

    # Go 130 (enough) times and print last two generations visually on terminal to check out how this looks like
    # Print it and chck by eye if somethig is repeating
    # Those looks the same, every next generation is just shifted to the right by 1
    # Okay so I know how many plants are going to be in generation 50 bilions
    # I need to get a difference between two lasts generation because that difference is going to be the same
    lucky_guess_generations = 130
    prior_to_last_result = 0
    last_result = 0
    difference = 0
    for i in range(lucky_guess_generations):
        indexes = runMutation(indexes, mutations)
        # uncommenting to check out if two last generations are different
        # if i == lucky_guess_generations - 2 or i == lucky_guess_generations -1:
            # indexes_to_string_represntation = ''.join('#' if index in indexes else '.' for index in range(-10, 500))
            # print(indexes_to_string_represntation)
        if i == lucky_guess_generations - 2:
            prior_to_last_result = sum(indexes)
        if i == lucky_guess_generations - 1:
            last_result = sum(indexes)
            
    current_sum = sum(indexes)
    difference = last_result - prior_to_last_result
    # formula is simple: take what you already computed
    # add how many generations are there left to run and multiple it by difference because difference is going to be the same
    sum_total = current_sum + ((50000000000 - lucky_guess_generations) * difference)
    print(sum_total)
main()