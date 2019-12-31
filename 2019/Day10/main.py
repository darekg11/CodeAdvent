# Thanks to the Reddit community explaining the atan2 approach - pretty clever

import math

ASTEROID = '#'
ASTEROID_INDEX = 200

def laser_atan(x, y):
    ang = math.atan2(x, y)
    # atan2 is designetated from -PI to +PI and we need it from 0 to 2PI to have 360 degrees
    if ang < 0:
        ang += 2 * math.pi
    # make atan clockwise as laser is because by default it is counter-clockwise
    if ang != 0:
        ang = 2 * math.pi - ang
    return ang

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
    # atan2 function is going to return the same value for the coords that are based on the same vector direction
    # for example cx-x and cy-y giving following results pair [1, 2] and [2, 4] will give the same results
    # meaning we have second asteroid hidden behind other so only keep unique value making it only count visible asteroids
    # [ 1,2 ] == 0.463647609001
    # [ 2,4 ] == 0.463647609001
    asteroid_count_max, asteroid_x, asteroid_y = max((len(set(math.atan2(grid_x - x, grid_y - y) for grid_x, grid_y in grid)), x,y) for x,y in grid)
    print('Part 1:', asteroid_count_max)

    # Start Part 2:
    # First, drop asteroid on which is the station
    grid.remove((asteroid_x, asteroid_y))
    # Start laser in undefined position, can't be 0 since 0 is going to be already first rotation
    last_angle = -1
    current_asteroid_index = 0
    # Keep referening destroyed asteroids
    asteroid_destroyed_x = None
    asteroid_destroyed_y = None
    while current_asteroid_index < ASTEROID_INDEX:
        angle = 5
        for cx, cy in grid:
            ang = laser_atan(asteroid_x-cx, asteroid_y-cy)
            if ang > last_angle and ang < angle:
                asteroid_destroyed_x = cx
                asteroid_destroyed_y = cy
                angle = ang
        grid.remove((asteroid_destroyed_x, asteroid_destroyed_y))
        last_angle = angle
        current_asteroid_index += 1

    print('Part 2:', asteroid_destroyed_x * 100 + asteroid_destroyed_y)

main()