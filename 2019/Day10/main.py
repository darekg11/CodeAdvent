import math
ASTEROID = '#'

def build_asteroid_grid(filename):
    grid = set()
    file_handle = open(filename)
    lines = file_handle.readlines()
    for height, single_line in enumerate(lines):
        for widith, single_character in enumerate(single_line):
            if single_character == ASTEROID:
                grid.add((widith, height))
    return grid

def main():
    grid = build_asteroid_grid('input.txt')
    #atan2 function is going to return the same value for the coords that are based on the same sloope
    # for example cx-x and cy-y giving following results pair [1, 2] and [2, 4] will give the same results meaning
    # we have second asteroid hidden
    #1,2 == 0.463647609001
    #2,4 == 0.463647609001
    asteroid_count_max = max([ len(set(math.atan2(grid_x - x, grid_y - y) for grid_x, grid_y in grid)) for x,y in grid ])
    print(asteroid_count_max)

main()