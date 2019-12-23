from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

MOVE_UP = 'U'
MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'

MOVEMENT_TO_VECTOR = {
    MOVE_UP: Point(0, -1),
    MOVE_DOWN: Point(0, 1),
    MOVE_LEFT: Point(-1, 0),
    MOVE_RIGHT: Point(1, 0)
}

NO_WIRE = 'O'
WIRE = 'X'

CENTRAL_PORT_COORD = Point(0, 0)

def parse_wire_step(wire: str):
    return {
        'direction': wire[0],
        'steps': int(wire[1:])
    }

def map_wire_steps_into_structure(wires):
    return [ parse_wire_step(single_wire) for single_wire in wires ]

def calculate_new_position(current_vector, vector):
    return Point(current_vector.x + vector.x, current_vector.y + vector.y)

def generate_circut_map_for_wire(wire):
    wires_structure = map_wire_steps_into_structure(wire)
    points_chain = []
    current_position = Point(CENTRAL_PORT_COORD.x, CENTRAL_PORT_COORD.y)
    points_chain.append(current_position)
    for single_wire_step in wires_structure:
        direction = single_wire_step['direction']
        steps = single_wire_step['steps']
        vector = MOVEMENT_TO_VECTOR[direction]
        for single_step in range(steps):
            new_position = calculate_new_position(current_position, vector)
            current_position = new_position
            points_chain.append(Point(new_position.x, new_position.y))
    return points_chain

def manhatan_distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def readLinesFromFileAndReturnThemInArray(filename):
    fo = open(filename, "r+")
    lines = fo.readlines()
    fo.close()
    return lines

def part_1():
    wires = readLinesFromFileAndReturnThemInArray('input.txt')
    first_wire = wires[0].split(',')
    second_wire = wires[1].split(',')

    first_wire_circut = set(generate_circut_map_for_wire(first_wire))
    second_wire_circut = set(generate_circut_map_for_wire(second_wire))
    crossing_points = first_wire_circut.intersection(second_wire_circut)

    distance_for_every_crossing_point = [ manhatan_distance(CENTRAL_PORT_COORD.x, point.x, CENTRAL_PORT_COORD.y, point.y) for point in crossing_points ] 
    distance_for_every_crossing_point.sort()
    # Do not include first one as this is 0,0 aka CENTRAL POINT
    smallest_distance = distance_for_every_crossing_point[1]
    print('Part 1:', smallest_distance)

def part_2():
    wires = readLinesFromFileAndReturnThemInArray('input.txt')
    first_wire = wires[0].split(',')
    second_wire = wires[1].split(',')

    first_wire_circut = generate_circut_map_for_wire(first_wire)
    second_wire_circut = generate_circut_map_for_wire(second_wire)
    first_wire_circut_set = set(generate_circut_map_for_wire(first_wire))
    second_wire_circut_set = set(generate_circut_map_for_wire(second_wire))
    crossing_points = first_wire_circut_set.intersection(second_wire_circut_set)
    # Drop 0, 0 starting point
    crossing_points_without_starting_point = [ single_point for single_point in crossing_points if single_point.x != 0 and single_point.y != 0 ]
    # Steps are just next indexes of generated circut array - find matching points in array and return indexes for both circuts
    steps_sum = []
    for intersection_coord in crossing_points_without_starting_point:
        first_wire_circut_steps = next((i for i, item in enumerate(first_wire_circut) if item.x == intersection_coord.x and item.y == intersection_coord.y), -1)
        second_wire_circut_steps = next((i for i, item in enumerate(second_wire_circut) if item.x == intersection_coord.x and item.y == intersection_coord.y), -1)
        steps_sum.append(first_wire_circut_steps + second_wire_circut_steps)
    minimal_steps = min(steps_sum)
    print('Part 2:', minimal_steps)


part_1()
part_2()