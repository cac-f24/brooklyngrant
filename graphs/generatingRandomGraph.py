import networkx as nx
import matplotlib.pyplot as plt
import random

# Create a random undirected graph.
# Default with 10 nodes and with a 30% 
# probability that each edge exists between 
# any pair of nodes
def generateRandomGraph(num_nodes=10, edge_prob=0.3):
    G = nx.gnp_random_graph(num_nodes, edge_prob, seed=random.randint(1, 100))
    
    # make sure all nodes have at least one edge
    for node in G.nodes:
        if G.degree[node] == 0:
            target = random.choice([n for n in G.nodes if n != node]) # pick random node
            G.add_edge(node, target) #add edge
    
    return G

# Main
G = generateRandomGraph()
print(f"Generated Graph with {len(G.nodes)} nodes and {len(G.edges)} edges.")

nx.draw(G, with_labels=True)
plt.show()