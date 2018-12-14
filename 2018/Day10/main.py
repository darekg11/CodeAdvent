import re
def getDataFromInputFile(filename):
    inputFile = open(filename, 'r')
    lines = inputFile.readlines()
    inputFile.close()
    return [[int(singleValue) for singleValue in re.findall(r'-?\d+', singleLine)] for singleLine in lines]

# What this is goign to do is a pretty basic and not really adjusted to I guess more complicated stuff but
# It will go through every second starting 0 to max_seconds - 1 and will calculate each point final position after that seconds
# And get the second when bound box of created stars is the smallest, hoping that is the same as getting some text
def findSecondWhenTheBoundBoxOfStartsIsTheSmallest(data, max_seconds):
    min_bound_box = None
    the_best_second = None
    min_x_best = None
    max_x_best = None
    min_y_best = None
    max_y_best = None
    for second in range(max_seconds):
        min_x = min([pos_x + second * vel_x for (pos_x, pos_y, vel_x, vel_y) in data])
        max_x = max([pos_x + second * vel_x for (pos_x, pos_y, vel_x, vel_y) in data])
        min_y = min([pos_y + second * vel_y for (pos_x, pos_y, vel_x, vel_y) in data])
        max_y = max([pos_y + second * vel_y for (pos_x, pos_y, vel_x, vel_y) in data])
        bound_box = max_x - min_x + max_y - min_y
        if min_bound_box is None or bound_box < min_bound_box:
            min_bound_box = bound_box
            the_best_second = second
            min_x_best = min_x
            max_x_best = max_x
            min_y_best = min_y
            max_y_best = max_y
    return the_best_second, min_x_best, max_x_best, min_y_best, max_y_best

def main():
    # Parse the input
    data = getDataFromInputFile('input.txt')

    # Try to guess second where bound box is the smallest, lets try after 30000 seconds
    # CPU Fans 100% POWER LETS GO
    desired_second, min_x, max_x, min_y, max_y = findSecondWhenTheBoundBoxOfStartsIsTheSmallest(data, 30000)
    # +1 because if max_x = 2 and min_x = 1 that would give 1 but there are two columns really
    columns = max_x - min_x + 1
    rows = max_y - min_y + 1
    # Generate word table filled with ' ' at the beggining
    word_table =  [[' ' for column in range(columns)] for row in range(rows)]
    for (pos_x, pos_y, vel_x, vel_y) in data:
        word_table[pos_y + desired_second * vel_y - min_y][pos_x + desired_second * vel_x - min_x] = '*'

    # Part 1
    for row in word_table:
        print(''.join(row))
    
    # Part 2
    print(desired_second)
main()