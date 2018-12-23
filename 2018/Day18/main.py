OPEN_GROUND = '.'
TREE = '|'
LUMBERYARD = '#'

from collections import defaultdict

def read_region_data_from_file(filename):
    # 2d map [y][x]
    map_layout = []
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    for single_line in lines:
        single_line_dropped_line_end = single_line.replace('\n', '')
        map_row = []
        for single_row in single_line_dropped_line_end:
            map_row.append(single_row)
        map_layout.append(map_row)
    return map_layout

def get_adjacent_cells(cell_x, cell_y, map_layout, size):
    # Let's only store the type
    adjacent_cells = []
    # [y - 1][x - 1]
    if cell_y - 1 >= 0 and cell_x -1 >= 0:
        adjacent_cells.append(map_layout[cell_y - 1][cell_x - 1])
    # [y - 1][x]
    if cell_y - 1 >= 0:
        adjacent_cells.append(map_layout[cell_y - 1][cell_x])
    # [y - 1][x + 1]
    if cell_y - 1 >= 0 and cell_x + 1 < size:
        adjacent_cells.append(map_layout[cell_y - 1][cell_x + 1])
    # [y][x - 1]
    if cell_x - 1 >= 0:
        adjacent_cells.append(map_layout[cell_y][cell_x - 1])
    # [y][x + 1]
    if cell_x + 1 < size:
        adjacent_cells.append(map_layout[cell_y][cell_x + 1])
    # [y + 1][x + 1]
    if cell_y + 1 < size and cell_x + 1 < size:
        adjacent_cells.append(map_layout[cell_y + 1][cell_x + 1])
    # [y + 1][x]
    if cell_y + 1 < size:
        adjacent_cells.append(map_layout[cell_y + 1][cell_x])
    # [y + 1][x - 1]
    if cell_y + 1 < size and cell_x - 1 >= 0:
        adjacent_cells.append(map_layout[cell_y + 1][cell_x - 1])
    return adjacent_cells

def determine_outcome_of_cell(cell_x, cell_y, map_layout, size):
    adjacent_cells = get_adjacent_cells(cell_x, cell_y, map_layout, size)
    if map_layout[cell_y][cell_x] == OPEN_GROUND:
        return TREE if adjacent_cells.count(TREE) >= 3 else OPEN_GROUND
    if map_layout[cell_y][cell_x] == TREE:
        return LUMBERYARD if adjacent_cells.count(LUMBERYARD) >= 3 else TREE
    if map_layout[cell_y][cell_x] == LUMBERYARD:
        return LUMBERYARD if adjacent_cells.count(LUMBERYARD) >= 1 and adjacent_cells.count(TREE) >= 1 else OPEN_GROUND


def execute_magic(map_layout, size):
    # create new empty grid
    # We have an empty grid that we will fill bsaed on current map_layout
    new_grid = [[0 for x in range(size)] for y in range(size)]
    # Go trought every cell
    for y in range(size):
        for x in range(size):
            # for every cell execute magic
            new_grid[y][x] = determine_outcome_of_cell(x, y, map_layout, size)
    return new_grid


def main():
    # Get map layout from file
    map_layout = read_region_data_from_file('input.txt')

    # Map size, assume that it is a sqaure
    size_of_map = len(map_layout[0])

    # Part 1 - 10 minutes
    MINUTES_THRESHOLD_PART_1 = 10
    
    # Run magic
    for _minute in range(MINUTES_THRESHOLD_PART_1):
        map_layout = execute_magic(map_layout, size_of_map)
    
    wooded_acres = 0
    lumberyard_acres = 0
    for y in range(size_of_map):
        for x in range(size_of_map):
            if map_layout[y][x] == TREE:
                wooded_acres += 1
            if map_layout[y][x] == LUMBERYARD:
                lumberyard_acres += 1
    
    # Part 1
    print(wooded_acres * lumberyard_acres)

    # Part 2 - crazy value as always, fuck let's try brute force it but it won't wok for 101% but wort trying
    # Okay, it is impossible to do it quickly with brute force, hmm
    # Okay, we need to check if the same 
    # Get map layout from file
    map_layout = read_region_data_from_file('input.txt')

    # Map size, assume that it is a sqaure
    size_of_map = len(map_layout[0])

    # Part 2 - 10 minutes
    MINUTES_THRESHOLD_PART_2 = 1000000000

    # It will store the map as one string and minute where it happen
    already_seen_patterns = defaultdict()
    
    # Run magic and look out for pattern duplications
    for minute in range(MINUTES_THRESHOLD_PART_2):
        map_layout = execute_magic(map_layout, size_of_map)
        map_layout_as_string = ''.join(str(item) for innerlist in map_layout for item in innerlist)
        duplicate_detection = already_seen_patterns.get(map_layout_as_string)
        # Found duplication
        if duplicate_detection is not None:
            # Subtract current minute from time when duplicate was found
            period_of_looping = minute - duplicate_detection
            # Add 1 to current minute as loop starts
            current_minute = minute + 1
            # Keep on adding period of looping
            while current_minute < MINUTES_THRESHOLD_PART_2:
                current_minute += period_of_looping
            # subtract one period as we might went over the limit
            current_minute -= period_of_looping
            # now jut run it with current grid and remainig minutes and we will have answer
            for _second_attempt in range(MINUTES_THRESHOLD_PART_2 - current_minute):
                map_layout = execute_magic(map_layout, size_of_map)
            # okay, we should be done - break the loop
            break
        else:
            already_seen_patterns[map_layout_as_string] = minute

    wooded_acres = 0
    lumberyard_acres = 0
    for y in range(size_of_map):
        for x in range(size_of_map):
            if map_layout[y][x] == TREE:
                wooded_acres += 1
            if map_layout[y][x] == LUMBERYARD:
                lumberyard_acres += 1
    
    # Part 2
    print(wooded_acres * lumberyard_acres)    


main()