import networkx as nx
from brooklyngrant.graphs.generatingRandomGraph import generateRandomGraph
import random

def bfsTraversal(G):
    bfs_traversal = list(nx.bfs_edges(G, startNode))
    return bfs_traversal

def dfsTraversal(G):
    dfs_traversal = list(nx.dfs_edges(G, startNode))
    return dfs_traversal

# Main
G = generateRandomGraph()
startNode = random.choice(list(G.nodes))

# BFS traversal
bfsEdges = bfsTraversal(G)
print(f"BFS starting from node {startNode}: {bfsEdges}")

# DFS traversal
dfsEdges = dfsTraversal(G)
print(f"DFS starting from node {startNode}: {dfsEdges}")
