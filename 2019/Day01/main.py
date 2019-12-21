import math

def readNumbersFromFileAndReturnThemInArray(filename):
    numbers = []
    with open(filename) as inputFile:
        for singleLine in inputFile:
            singleLine = singleLine.split()
            if (singleLine != ''):
                numbers.append(int(singleLine[0]))
    return numbers

def calculate_fuel(mass):
    return math.floor(mass / 3) - 2

def calculate_fuel_requirement_per_module(mass):
    total = 0
    mass_to_calculate = mass
    while True:
        fuel_requriement = calculate_fuel(mass_to_calculate)
        if fuel_requriement <= 0:
            break
        mass_to_calculate = fuel_requriement
        total += fuel_requriement
    return total 

def main():
    numbers = readNumbersFromFileAndReturnThemInArray("input.txt")
    # Part 1
    fuel_requirement_total = sum([ calculate_fuel(single_number) for single_number in numbers])
    print('Part 1:', fuel_requirement_total)

    # Part 2:
    fuel_requirement_total = sum([ calculate_fuel_requirement_per_module(single_module) for single_module in numbers])
    print('Part 2:', fuel_requirement_total)

main()