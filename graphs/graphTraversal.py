import argparse
import networkx as nx
import matplotlib.pyplot as plt
from graphGenerator import generateUnweightedGraph
import random

## Graph traversal algorithm BFS
def bfsTraversal(G, start):
    bfs_traversal = list(nx.bfs_edges(G, start))
    return bfs_traversal

## Graph traversal algorithm DFS
def dfsTraversal(G, start):
    dfs_traversal = list(nx.dfs_edges(G, start))
    return dfs_traversal

# Main
parser = argparse.ArgumentParser(description="Graph Traversal in Unweighted Graph")
parser.add_argument("--directed", action="store_true", help="Generate a directed graph")
args = parser.parse_args()

G = generateUnweightedGraph(directed=args.directed)
startNode = random.choice(list(G.nodes)) # randomly choose starting for now

# BFS traversal
bfsEdges = bfsTraversal(G, startNode)
print(f"BFS starting from node {startNode}: {bfsEdges}")

# DFS traversal
dfsEdges = dfsTraversal(G, startNode)
print(f"DFS starting from node {startNode}: {dfsEdges}")


# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))  # Two subplots in one row

# Positions for all nodes (use the same layout for both subplots)
pos = nx.spring_layout(G)

# BFS traversal plot
nx.draw(G, pos, ax=ax1, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)
nx.draw_networkx_edges(G, pos, edgelist=bfsEdges, edge_color="blue", width=2, style="dashed", ax=ax1)
ax1.set_title(f"BFS Traversal Starting from Node {startNode}")

# DFS traversal plot
nx.draw(G, pos, ax=ax2, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)
nx.draw_networkx_edges(G, pos, edgelist=dfsEdges, edge_color="green", width=2, style="solid", ax=ax2)
ax2.set_title(f"DFS Traversal Starting from Node {startNode}")

plt.show()
