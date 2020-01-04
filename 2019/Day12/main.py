import re
import math
from copy import deepcopy
from collections import defaultdict

X_INDEX = 0
Y_INDEX = 1
Z_INDEX = 2

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def readInput(filename):
    inputFile = open(filename, 'r')
    lines = inputFile.readlines()
    inputFile.close()
    return [ { 'index': index, 'velocity': [0, 0, 0], 'position': [int(singleValue) for singleValue in re.findall(r'-?\d+', singleLine)]} for index, singleLine in enumerate(lines)]

def time_lapse(moons):
    # Calculate velocities
    for first_moon in moons:
        for second_moon in moons:
            for axis in range(X_INDEX, Z_INDEX + 1):
                if first_moon['position'][axis] > second_moon['position'][axis]:
                    first_moon['velocity'][axis] -= 1
                if first_moon['position'][axis] < second_moon['position'][axis]:
                    first_moon['velocity'][axis] += 1
    # Update positions
    for moon in moons:
        for axis in range(X_INDEX, Z_INDEX + 1):
            moon['position'][axis] += moon['velocity'][axis]
    return moons

def simulation(moons, steps):
    for __ in range(0, steps):
        moons = time_lapse(moons)
    return moons

def calculate_energy_in_system(moons):
    total_energy = 0
    for single_moon in moons:
        potential_energy = 0
        kinetic_energy = 0
        for axis in range(X_INDEX, Z_INDEX + 1):
            potential_energy += abs(single_moon['position'][axis])
            kinetic_energy += abs(single_moon['velocity'][axis])
        total_energy += potential_energy * kinetic_energy
    return total_energy

def find_repeated_period_for_axis(initial_values, axis_index):
    moons = initial_values
    seen = set()
    steps = 0
    while True:
        moons = simulation(moons, 1)
        position_part_key = ''.join([ str(single_moon['position'][axis_index]) for single_moon in moons ])
        velocity_part_key = ''.join([ str(single_moon['velocity'][axis_index]) for single_moon in moons ])
        key = position_part_key + ":" + velocity_part_key
        if key in seen:
            break
        else:
            seen.add(key)
            steps += 1
    return steps

def main():
    initial_values = readInput('input.txt')
    moons_after_simulation = simulation(deepcopy(initial_values), 1000)
    total_energy = calculate_energy_in_system(moons_after_simulation)
    print('Part 1:', total_energy)

    # Part 2, find repeat cycle for each axis independiently and then use LCM to find answer for the system:
    # https://www.reddit.com/r/adventofcode/comments/e9j0ve/2019_day_12_solutions/falhle7?utm_source=share&utm_medium=web2x
    # Let's say X axis repeat after 5 times and Y axis repeat after 10 times then X and Y will repeat again after 50 times
    # so you need to find LCM of all three axis
    axis_x_repeat_period = find_repeated_period_for_axis(deepcopy(initial_values), X_INDEX)
    axis_y_repeat_period = find_repeated_period_for_axis(deepcopy(initial_values), Y_INDEX)
    axis_z_repeat_period = find_repeated_period_for_axis(deepcopy(initial_values), Z_INDEX)
    print('Part 2:', lcm(axis_x_repeat_period, lcm(axis_y_repeat_period, axis_z_repeat_period)))


main()