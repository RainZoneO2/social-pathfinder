import networkx as nx

def build_demo_graph():
    """Create a small hardcoded demo social network."""
    G = nx.Graph()
    G.add_nodes_from(["Alice", "Bob", "Charlie", "Diana", "John", "Emily", "Sarah", "David"])
    G.add_edges_from([("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "Diana"), ("Charlie", "Diana"), ("John", "Emily"), ("Sarah", "David")])
    return G

def print_graph_info(graph):
    """Print basic information about the graph."""
    print(f"{graph.number_of_nodes()} Nodes in the graph: {list(graph.nodes())}")
    print(f"{graph.number_of_edges()} Edges in the graph: {list(graph.edges())}")
    for node in list(graph.nodes())[:2]:
        print(f"Neighbors of {node}: {list(graph.adj[node])}")

if __name__ == "__main__":
    demo_graph = build_demo_graph()

    print_graph_info(demo_graph)