import networkx as graph_lib

def main():
    # https://networkx.github.io/documentation/stable/reference/classes/digraph.html
    graph = graph_lib.DiGraph()
    # Split each line
    data = [tuple(line.strip().split(")")) for line in open('input.txt', 'r')]
    # Add edges
    for single_orbit_pair in data:
        graph.add_edge(single_orbit_pair[0], single_orbit_pair[1])
    # ancestors call is returning all Nodes in Graph that connects to param
    # So loop thourgh all nodes, get their connected nodes -> get len and sum it all
    sum_of_orbits = sum([len(graph_lib.ancestors(graph, node)) for node in graph.nodes()])
    print('Part 1:', sum_of_orbits)
    # Part 2 is actually calculating shortest path from node YOU to node SAN and subtracting 2 because we need to get path of orbiting objects and not objects themselves
    shortest_path = graph_lib.shortest_path_length(graph.to_undirected(), "YOU", "SAN", 1) - 2
    print('Part 2:', shortest_path)

main()