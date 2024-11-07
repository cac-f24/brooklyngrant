import networkx as nx
import matplotlib.pyplot as plt
import random
import matplotlib.patches as mpatches

# Create a random undirected unweighted graph.
# Default with 10 nodes and with a 30% 
# probability that each edge exists between 
# any pair of nodes
def generateUnweightedGraph(num_nodes=10, edge_prob=0.3, directed=False):
    G = nx.gnp_random_graph(num_nodes, edge_prob, seed=random.randint(1, 100), directed=directed)
    
    if directed:
        G = nx.DiGraph(G)
    
    # make sure all nodes have at least one edge or at least one outgoing edge
    for node in G.nodes:
        if (directed and G.out_degree(node) == 0) or (not directed and G.degree(node) == 0):
            target = random.choice([n for n in G.nodes if n != node]) # random node that is not the current node
            G.add_edge(node, target)  # add edge
    
    print(f"Generated {'directed,' if directed else 'undirected,'} unweighted graph with {len(G.nodes)} nodes and {len(G.edges)} edges.")
    
    return G

# Create a random undirected weighted graph.
# Default with 10 nodes and with a 30% 
# probability that each edge exists between 
# any pair of nodes and a weight range of 1-10
def generateWeightedGraph(num_nodes=10, edge_prob=0.3, weight_range=(1, 10), directed=False):
    G = nx.gnp_random_graph(num_nodes, edge_prob, seed=random.randint(1, 100), directed=directed)

    if directed:
        G = nx.DiGraph(G)

    # Add weights to each edge
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(*weight_range)

    # Ensure all nodes have at least one outgoing (for directed) or undirected edge
    for node in G.nodes:
        if (directed and G.out_degree(node) == 0) or (not directed and G.degree(node) == 0):
            target = random.choice([n for n in G.nodes if n != node])
            G.add_edge(node, target)
            G.edges[node, target]['weight'] = random.randint(*weight_range)
    
    print(f"Generated {'directed,' if directed else 'undirected,'} weighted graph with {len(G.nodes)} nodes and {len(G.edges)} edges.")
    return G

# Draws the weighted graph with edge weights.
# Highlights path edges if provided
def drawWeightedGraph(G, path_edges=None, path_color="red", title="Weighted Graph"):
    directed = G.is_directed()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10, arrows=directed)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if path_edges:
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2, label="Shortest Path", arrows=directed)
        # legend with a red line to indicate the highlighted path
        red_line = mpatches.Patch(color=path_color, label="Path")
        plt.legend(handles=[red_line])

    plt.title(title)
    plt.show()

