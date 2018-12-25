import re
import networkx as graph_lib
from collections import defaultdict

def get_data_from_input_file(filename):
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    input_file.close()
    return [[int(single_value) for single_value in re.findall(r'-?\d+', single_line)] for single_line in lines]

def manhatan_distance(first_point, second_point):
    x1 = first_point[0]
    x2 = second_point[0]
    y1 = first_point[1]
    y2 = second_point[1]
    z1 = first_point[2]
    z2 = second_point[2]
    t1 = first_point[3]
    t2 = second_point[3]
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) + abs(t1 - t2)

def main():
    # Parse input
    data = get_data_from_input_file('input.txt')

    # Reparse each point to an unique index to use as edge
    point_to_index = defaultdict()

    for i in range(len(data)):
        point_to_index[(data[i][0], data[i][1], data[i][2], data[i][3])] = i

    # We will create a graph
    graph = graph_lib.Graph()

    for single_point in data:
        for single_point_inner in data:
            if manhatan_distance(single_point, single_point_inner) <= 3:
                first_x, first_y, first_z, first_t = single_point
                second_x, second_y, second_z, second_t = single_point_inner
                graph.add_edge(point_to_index[(first_x, first_y, first_z, first_t)], point_to_index[(second_x, second_y, second_z, second_t)])
    
    # Part - 1, just show number of connected components which represnts the constelations
    print(graph_lib.number_connected_components(graph))

    
   
main()