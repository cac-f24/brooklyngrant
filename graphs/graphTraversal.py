import networkx as nx
import matplotlib.pyplot as plt
from generatingRandomGraph import generateRandomGraph
import random

def bfsTraversal(G, start):
    bfs_traversal = list(nx.bfs_edges(G, start))
    return bfs_traversal

def dfsTraversal(G, start):
    dfs_traversal = list(nx.dfs_edges(G, start))
    return dfs_traversal

# Main
G = generateRandomGraph()
startNode = random.choice(list(G.nodes)) # randomly choose starting for now

# BFS traversal
bfsEdges = bfsTraversal(G, startNode)
print(f"BFS starting from node {startNode}: {bfsEdges}")

# DFS traversal
dfsEdges = dfsTraversal(G, startNode)
print(f"DFS starting from node {startNode}: {dfsEdges}")

# Plotting the graph
plt.figure(figsize=(10, 6))

# Positions for all nodes
pos = nx.spring_layout(G)

# Draw the graph with all edges
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)

# Highlight BFS traversal edges in blue
nx.draw_networkx_edges(G, pos, edgelist=bfsEdges, edge_color="blue", width=2, style="dashed", label="BFS")

# Highlight DFS traversal edges in green
nx.draw_networkx_edges(G, pos, edgelist=dfsEdges, edge_color="green", width=2, style="solid", label="DFS")

# Add a legend to show which color represents which traversal
plt.legend(["BFS (dashed)", "DFS (solid)"])

plt.title(f"Graph Traversal Starting from Node {startNode}")
plt.show()
