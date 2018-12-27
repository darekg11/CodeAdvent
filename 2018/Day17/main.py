from copy import deepcopy

EMPTY_TILE = 0
CLAY_WALL = 1
UNSETTLED_WATER = 2
SETTLED_WATER = 3

# Returns min_y, max_y, min_x, max_x from input data
def find_min_max_coords_from_input(filename):
    min_y = None
    max_y = None
    min_x = None
    max_x = None
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    for single_line in lines:
        single_line_without_line_ending = single_line.replace('\n', '')
        split_by_comma  = single_line_without_line_ending.split(',')
        coord = split_by_comma[0][0]
        if coord == 'x':
            # Get X value
            split_by_euqal = split_by_comma[0].split('=')
            x_value = int(split_by_euqal[1])
            if min_x is None:
                min_x = x_value
            if max_x is None:
                max_x = x_value
            min_x = min([min_x, x_value])
            max_x = max([max_x, x_value])

            # Get Y values from first..second sequence
            splt_by_euqal_range_coord = split_by_comma[1].split('=')
            split_by_range_chars = splt_by_euqal_range_coord[1].split('..')
            y_first = int(split_by_range_chars[0])
            y_second = int(split_by_range_chars[1])
            if min_y is None:
                min_y = y_first
            if max_y is None:
                max_y = y_first
            min_y = min([min_y, y_first, y_second])
            max_y = max([max_y, y_first, y_second])
        else:
            # Get Y value
            split_by_euqal = split_by_comma[0].split('=')
            y_value = int(split_by_euqal[1])
            if min_y is None:
                min_y = y_value
            if max_y is None:
                max_y = y_value
            min_y = min([min_y, y_value])
            max_y = max([max_y, y_value])

             # Get X values from first..second sequence
            splt_by_euqal_range_coord = split_by_comma[1].split('=')
            split_by_range_chars = splt_by_euqal_range_coord[1].split('..')
            x_first = int(split_by_range_chars[0])
            x_second = int(split_by_range_chars[1])
            if min_x is None:
                min_x = x_first
            if max_x is None:
                max_x = x_first
            min_x = min([min_x, x_first, x_second])
            max_x = max([max_x, x_first, x_second])

    return min_y, max_y, min_x, max_x
        
def create_map_from_input(filename, size):
    # 2d MAP [y][x]
    # Of given size, the size must always be greater than max_x and max_y
    map_layout = [[EMPTY_TILE for x in range(size)] for y in range(size)]
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    for single_line in lines:
        single_line_without_line_ending = single_line.replace('\n', '')
        split_by_comma  = single_line_without_line_ending.split(',')
        coord = split_by_comma[0][0]
        if coord == 'x':
            # Get X value
            split_by_euqal = split_by_comma[0].split('=')
            x_value = int(split_by_euqal[1])

            # Get Y values from first..second sequence
            splt_by_euqal_range_coord = split_by_comma[1].split('=')
            split_by_range_chars = splt_by_euqal_range_coord[1].split('..')
            y_first = int(split_by_range_chars[0])
            y_second = int(split_by_range_chars[1])
            for index in range(y_first, y_second + 1):
                map_layout[index][x_value] = CLAY_WALL
        else:
            # Get Y value
            split_by_euqal = split_by_comma[0].split('=')
            y_value = int(split_by_euqal[1])

             # Get X values from first..second sequence
            splt_by_euqal_range_coord = split_by_comma[1].split('=')
            split_by_range_chars = splt_by_euqal_range_coord[1].split('..')
            x_first = int(split_by_range_chars[0])
            x_second = int(split_by_range_chars[1])
            for index in range(x_first, x_second + 1):
                map_layout[y_value][index] = CLAY_WALL
    return map_layout

def print_map(map_layout, min_y, max_y, min_x, max_x, dump_to_file):
    file_instance = None
    if dump_to_file == True:
        file_instance = open('output.txt', 'x')
    print('MAP PRINTING - START')
    for y in range(max_y + 1):
        for x in range(min_x, max_x + 1):
            to_print = ''
            if map_layout[y][x] == EMPTY_TILE:
                to_print = '.'
            if map_layout[y][x] == CLAY_WALL:
                to_print = '#'
            if map_layout[y][x] == UNSETTLED_WATER:
                to_print = '|'
            if map_layout[y][x] == SETTLED_WATER:
                to_print = '~'
            print(to_print, end='')
            if dump_to_file == True:
                file_instance.write(to_print)
        print('')
        if dump_to_file == True:
            file_instance.write('\n')
    print('MAP PRINTING - FINISH')
    if dump_to_file == True:
        file_instance.close()

def run_simulation(map_layout, min_y, max_y, min_x, max_x):
    # Make a copy of map_layout
    map_layout_copy = deepcopy(map_layout)
    # This will run simulation
    # One iteration of simulation is trying to move SINGLE drop of water, first to the most bottom and then spread it to the right or left
    # Water drop always start from the spring which is at y = 0 and x = 500
    current_x = 500
    current_y = 0
    iteration_done = False
    while True:
        # print_map(map_layout_copy, min_y, max_y, min_x, max_x, False)
        # If iteration is completed but we haven't end the loop yet then we need to move current coords back to the spring to start with another drop
        if iteration_done:
            current_x = 500
            current_y = 0
            iteration_done = False
        # Move the fuck down if tile below is empty and we are withing limits of max_y
        while map_layout_copy[current_y + 1][current_x] == EMPTY_TILE and current_y <= max_y - 1:
            current_y += 1
        # Ok we are the at very bottom of things and we need to start with another water drop
        if current_y == max_y:
            # Mark that coords needs to be restarted during next iteration
            iteration_done = True
            # Mark last title as UNSETTLED_WATER aka flowing
            map_layout_copy[current_y][current_x] = UNSETTLED_WATER
            # Start next iteration so we don't have to add guard check to every condition below checking if we are within the bounds
            continue
        # We should skip those coords that are higher than out min value
        # As per puzzle description
        if current_y < min_y:
            # This also marks the end of our search because we start from the bottom
            # So as soon as we get here that means, we are done
            break
        
        # Okay we can no lomger move down, so we need to flow the water either to the left or to the right
        # # Determine movement, left wins in priority
        horizontal_movement = 'NOT_POSSIBLE'
        if map_layout_copy[current_y][current_x - 1] == EMPTY_TILE:
            horizontal_movement = 'LEFT'
        elif map_layout_copy[current_y][current_x + 1] == EMPTY_TILE:
            horizontal_movement = 'RIGHT'
        if horizontal_movement in ['LEFT', 'RIGHT']:
                movement_interval = -1 if horizontal_movement == 'LEFT' else 1
                # we can move to the left / right as long as next tile to the left / right is empty
                # and one tile under is either a clay wall or settled water
                while map_layout_copy[current_y][current_x + movement_interval] == EMPTY_TILE and (map_layout_copy[current_y + 1][current_x] == CLAY_WALL or map_layout_copy[current_y + 1][current_x] == SETTLED_WATER):
                    current_x += movement_interval
        # At this point we should be at the best location

        # We need to somehow correctly mark unsettled water because with current approach some tiles might have been marked as settled water
        # while in reality it will have to be unsettled
        # if any tile in range of current tile is UNSETTLED
        if map_layout_copy[current_y + 1][current_x] != EMPTY_TILE:
            if map_layout_copy[current_y + 1][current_x] == UNSETTLED_WATER or map_layout_copy[current_y][current_x + 1] == UNSETTLED_WATER or map_layout_copy[current_y][current_x - 1] == UNSETTLED_WATER:
                # then current tile also is UNSETTLED
                map_layout_copy[current_y][current_x] = UNSETTLED_WATER
                # Clear every SETTLED WATER to the left and right as UNSETLLED
                x = current_x
                # Start left
                while map_layout_copy[current_y][x - 1] == SETTLED_WATER:
                    map_layout_copy[current_y][x - 1] = UNSETTLED_WATER
                    x -= 1
                x = current_x
                # Now right
                while map_layout_copy[current_y][x + 1] == SETTLED_WATER:
                    map_layout_copy[current_y][x + 1] = UNSETTLED_WATER
                    x += 1
            else:
                map_layout_copy[current_y][current_x] = SETTLED_WATER
            # Iteration is done
            iteration_done = True
        
    return map_layout_copy

def main():
    TEST_DATA = False
    # 2000 x 2000. 2000 is greater than mine max_x and max_y
    MY_GRID_SIZE = 2000

    filename_to_use = 'test-input.txt' if TEST_DATA is True else 'input.txt'
    # Get dimensions - will be useful when debugging the map via printing to minimize to output
    min_y, max_y, min_x, max_x =  find_min_max_coords_from_input(filename_to_use)
    # Fill the map with clays
    map_layout = create_map_from_input(filename_to_use, MY_GRID_SIZE)
    
    map_layout = run_simulation(map_layout, min_y, max_y, min_x, max_x)

    # print_map(map_layout, min_y, max_y, min_x, max_x, True)
    # Part 1 - find all stale or flowing water points
    sum_of_tiles = 0
    for y in range(MY_GRID_SIZE):
        for x in range(MY_GRID_SIZE):
            if map_layout[y][x] == UNSETTLED_WATER or map_layout[y][x] == SETTLED_WATER:
                sum_of_tiles += 1
    print('Part 1: ', sum_of_tiles)

    # Part 2 - find only stale water points
    sum_of_tiles = 0
    for y in range(MY_GRID_SIZE):
        for x in range(MY_GRID_SIZE):
            if map_layout[y][x] == SETTLED_WATER:
                sum_of_tiles += 1
    print('Part 2: ', sum_of_tiles)

main()