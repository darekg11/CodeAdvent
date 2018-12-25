import networkx as graph_library
import re
from collections import defaultdict

X_POSITION_INDEX = 0
Y_POSITION_INDEX = 1
Z_POSITION_INDEX = 2
RANGE_INDEX = 3
USER_POSITION = [0, 0, 0, 0]

def get_data_from_input_file(filename):
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    input_file.close()
    return [[int(single_value) for single_value in re.findall(r'-?\d+', single_line)] for single_line in lines]

def manhatan_distance(first_point, second_point):
    x1 = first_point[X_POSITION_INDEX]
    x2 = second_point[X_POSITION_INDEX]
    y1 = first_point[Y_POSITION_INDEX]
    y2 = second_point[Y_POSITION_INDEX]
    z1 = first_point[Z_POSITION_INDEX]
    z2 = second_point[Z_POSITION_INDEX]
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)

def main():
    # Part - 1
    # read the input data
    data = get_data_from_input_file('input.txt')
    # get nanobot with strongest signal
    nanobot_with_maximum_radius = max(data, key=lambda k: k[RANGE_INDEX])
    # get all in distance
    nanobots_in_range_of_strongest = [nanobot for nanobot in data if manhatan_distance(nanobot, nanobot_with_maximum_radius) <= nanobot_with_maximum_radius[RANGE_INDEX]]
    # Part 1 solution
    print(len(nanobots_in_range_of_strongest))

    # Part - 2
    # NOTE: Thanks to great people at reddit code-advent introducing me to awesome networkx and showing possibilites of this library
    # Also to user kingfishr for mentioning Bron-Kerbosh algorithm

    # read the input data
    data = get_data_from_input_file('input.txt')
    # build a graph with edges between overlapping nanobots
    graph = graph_library.Graph()
    # number each nanobot with ID used as nodes
    nanos = defaultdict()
    for bot_index in range(len(data)):
        nanos[(data[bot_index][X_POSITION_INDEX], data[bot_index][Y_POSITION_INDEX], data[bot_index][Z_POSITION_INDEX], data[bot_index][RANGE_INDEX])] = bot_index
    # Go through every bot
    for bot in data:
        # find all overlaps  between current bot and every other
        # two nanobots overlap if distance between them is equal or smaller to sum of ranges
        # this includes the current bot itself
        overlapping_bots = [other_bot for other_bot in data if manhatan_distance(bot, other_bot) <= bot[RANGE_INDEX] + other_bot[RANGE_INDEX]]
        for overlapping in overlapping_bots:
            # Add every overlapping node to graph
            # from current_bot_index to overlapping_node_index
            current_bot_index = nanos[(bot[X_POSITION_INDEX], bot[Y_POSITION_INDEX], bot[Z_POSITION_INDEX], bot[RANGE_INDEX])]
            overlapping_bot_index = nanos[(overlapping[X_POSITION_INDEX], overlapping[Y_POSITION_INDEX], overlapping[Z_POSITION_INDEX], overlapping[RANGE_INDEX])]
            graph.add_edge(current_bot_index, overlapping_bot_index)

    # Based on the algorithm published by Bron & Kerbosch (1973) as adapted by Tomita, Tanaka and Takahashi (2006)
    # and discussed in Cazals and Karande (2008).
    # The method essentially unrolls the recursion used in the references to avoid issues of recursion stack depth.
    # This find all overlapping subgraphs
    cliques = list(graph_library.find_cliques(graph))

    # select the largest sub-graph
    clique = max(cliques, key=len)

    # remap ids of nanobots to actual 
    clique_ids_to_actual_nanobots_coords = []
    for coords, id_nano in nanos.items():
        if id_nano in clique:
            clique_ids_to_actual_nanobots_coords.append(coords)
    
    surfaces = [manhatan_distance(USER_POSITION, bot) - bot[RANGE_INDEX] for bot in clique_ids_to_actual_nanobots_coords]

    # the furthest away surface point is the minimum manhattan distance
    print(max(surfaces))
main()
