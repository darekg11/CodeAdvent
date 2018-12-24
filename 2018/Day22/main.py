import networkx as tools

# Inputs
INPUT_DEPTH = 8103
TARGET_X = 9
TARGET_Y = 758

# Constants
GEOLOGICAL_INDEX_VALUE = 0
EROSION_INDEX_VALUE = 1
RISK_INDEX_VALUE = 2

ROCKS = 0
WET = 1
NARROW = 2

TORCH = 0
ROPE = 1
NEITHER = 2

TIME_TO_CHANGE_EQUIPMENT = 7

POSSBIBLE_ITEMS_TO_USE_PER_REGION = {
    ROCKS: (TORCH, ROPE),
    WET: (ROPE, NEITHER),
    NARROW: (TORCH, NEITHER)
}

PART_2_EXTRA_MARGIN = 150

def create_maze(depth, x, y):
    maze = {}
    for y_coord in range(0, y + 1):
        for x_coord in range(0, x + 1):
            geological_index = 0
            # if coords are 0,0 or coords are at target position
            if (x_coord == 0 and y_coord == 0) or (x_coord == x and y_coord == y):
                geological_index = 0
            elif y_coord == 0:
                geological_index = x_coord * 16807
            elif x_coord == 0:
                geological_index = y_coord * 48271
            else:
                geological_index = maze[(x_coord - 1, y_coord)][EROSION_INDEX_VALUE] * maze[(x_coord, y_coord - 1)][EROSION_INDEX_VALUE]
            erosion_value = (geological_index + INPUT_DEPTH) % 20183
            risk_level =  erosion_value % 3
            maze[(x_coord, y_coord)] = (geological_index, erosion_value, risk_level)
    return maze

def generate_adjacents_vectors(pos_x, pos_y):
    return [[pos_x, pos_y - 1], [pos_x, pos_y + 1], [pos_x - 1, pos_y], [pos_x + 1, pos_y]]

# max_corner_x a nd max_cor
def calculate_shortest_path(maze, target_x, target_y):
    # PART_2_EXTRA_MARGIN is additional max width and heigh beyond target because per puzzle description:
    # The fastest route might involve entering regions beyond the X or Y coordinate of the target.
    max_corner_x = target_x + PART_2_EXTRA_MARGIN
    max_corner_y = target_y + PART_2_EXTRA_MARGIN
    graph = tools.Graph()
    for y_coord in range(0, max_corner_y + 1):
        for x_coord in range(0, max_corner_x + 1):
            items_that_can_be_used = POSSBIBLE_ITEMS_TO_USE_PER_REGION[maze[(x_coord, y_coord)][RISK_INDEX_VALUE]]
            first_possible_item = items_that_can_be_used[0]
            second_possible_item = items_that_can_be_used[1]
            # Add edge from the same position but with differnt tools so we know what kind of tools we can use of that x,y
            # Add weight equal to time required to change equipment
            graph.add_edge((x_coord, y_coord, first_possible_item), (x_coord, y_coord, second_possible_item), weight = TIME_TO_CHANGE_EQUIPMENT)
            # Check adjacent cells and check what kind of items are required there
            adjacent_vectors = generate_adjacents_vectors(x_coord, y_coord)
            for single_vector in adjacent_vectors:
                vector_x = single_vector[0]
                vector_y = single_vector[1]
                if vector_x >= 0 and vector_x <= max_corner_x and vector_y >= 0 and vector_y <= max_corner_y:
                    # generate valid items here
                    items_that_can_be_used_here = POSSBIBLE_ITEMS_TO_USE_PER_REGION[maze[(vector_x, vector_y)][RISK_INDEX_VALUE]]
                    # Okay so now we need what items can be used at next adjacent location and what items I have in one coord before
                    # Make two sets, one of items that can be used before and one from that can be used right now as in adjacent cell
                    # If we have the same, here and there that (intersection of sets) that means equipped before items is the same that can be used now
                    # and therefore cost is only 1 minute of such nodes
                    for usable_item in set(items_that_can_be_used).intersection(set(items_that_can_be_used_here)):
                        graph.add_edge((x_coord, y_coord, usable_item), (vector_x, vector_y, usable_item), weight = 1)
    
    # Graph is created
    # Now use  Djikstra algorithm to find the shortest path between enter and targer position - we must start with torch and end with torch
    return tools.dijkstra_path_length(graph, (0, 0, TORCH), (target_x, target_y, TORCH))

def main():
    # Part  - 1
    # Cerate maze with each block having values GEOLOGICAL_INDEX, EROSION_VALUE and RISK_LEVEL
    maze = create_maze(INPUT_DEPTH, TARGET_X, TARGET_Y)
    sum_of_risk = sum(single_block[RISK_INDEX_VALUE] for single_block in maze.values())
    print(sum_of_risk)

    # Part - 2
    # Thanks to Reddit users sharing the solutions and helping me discover new libraries such as networkx
    maze = create_maze(INPUT_DEPTH, TARGET_X + PART_2_EXTRA_MARGIN, TARGET_Y + PART_2_EXTRA_MARGIN)
    print(calculate_shortest_path(maze, TARGET_X, TARGET_Y))

main()
