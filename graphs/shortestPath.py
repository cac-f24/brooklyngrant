import argparse
from graphGenerator import generateWeightedGraph, drawWeightedGraph
import networkx as nx
import random

## Find the shortest path between two nodes in a weighted graph
def findShortestPathWithDijkstra(G, start, target):
    try:
        # calculate the shortest path and its length
        path = nx.dijkstra_path(G, start, target, weight='weight')
        path_length = nx.dijkstra_path_length(G, start, target, weight='weight')
        return path, path_length
    except nx.NetworkXNoPath:
        print(f"No path exists between node {start} and node {target}.")
        return None, float('inf')

# Main
parser = argparse.ArgumentParser(description="Shortest Path in Weighted Graph")
parser.add_argument("--directed", action="store_true", help="Generate a directed graph")
args = parser.parse_args()

G = generateWeightedGraph(directed=args.directed)

# random start and target nodes
startNode = random.choice(list(G.nodes))
targetNode = random.choice([node for node in G.nodes if node != startNode])

# find shortest path between startNode and targetNode
path, path_length = findShortestPathWithDijkstra(G, startNode, targetNode)

# output the shortest path details
if path:
    print(f"Shortest path from node {startNode} to node {targetNode}: {path} with length {path_length}")
    path_edges = list(zip(path, path[1:]))
    # draw the weighted graph and highlight the shortest path
    drawWeightedGraph(G, path_edges=path_edges, title=f"Shortest Path from Node {startNode} to Node {targetNode}")
else:
    print(f"No path found from node {startNode} to node {targetNode}.")
