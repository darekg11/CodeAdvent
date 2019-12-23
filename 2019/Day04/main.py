RANGE_MIN = 206938
RANGE_MAX = 679128

def is_correct_part1(number: int):
    number_as_string = str(number)
    found_double = False
    for index in range(len(number_as_string) - 1):
        if found_double is False and number_as_string[index] == number_as_string[index + 1]:
            found_double = True
        if int(number_as_string[index + 1]) < int(number_as_string[index]):
            return False
    return found_double

def is_correct_part2(number: int):
    number_as_string = str(number)
    counter = 1
    for index in range(1, len(number_as_string)):
        if number_as_string[index] == number_as_string[index - 1]:
            counter += 1
        elif counter == 2:
            break
        else:
            counter = 1
    return counter == 2

def part_1():
    possible_counter = 0
    for i in range(RANGE_MIN, RANGE_MAX + 1):
        if is_correct_part1(i):
            possible_counter += 1
    print('Part 1:', possible_counter)

def part_2():
    possible_counter = 0
    for i in range(RANGE_MIN, RANGE_MAX + 1):
        if is_correct_part1(i) and is_correct_part2(i):
            possible_counter += 1
    print('Part 2:', possible_counter)

part_1()
part_2()