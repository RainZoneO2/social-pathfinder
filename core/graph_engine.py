import networkx as nx

def build_demo_graph() -> nx.Graph:
    """Create a small hardcoded demo social network."""
    G = nx.Graph()
    G.add_nodes_from([("Alice", { "followers":20 }), ("Bob", { "followers":15 }), 
                      ("Charlie", { "followers":10 }), ("Diana", { "followers":25 }), 
                      ("John", { "followers":30 }), ("Emily", { "followers":18 }), 
                      ("Sarah", { "followers":22 }), ("David", { "followers":12 })])
    G.add_edges_from([("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "Diana"), 
                      ("Charlie", "Diana"), ("John", "Diana"), ("John", "Emily"), 
                      ("Sarah", "Emily"), ("Sarah", "David")])
    return G

def assign_edge_weights(graph: nx.Graph) -> None:
    """Assign weights to edges based on the number of followers of the connected nodes."""
    for u, v in graph.edges():
        followers_u = graph.nodes[u]["followers"]
        followers_v = graph.nodes[v]["followers"]
        graph.edges[u, v]["weight"] = followers_u + followers_v

def print_graph_info(graph: nx.Graph) -> None:
    """Print basic information about the graph."""
    print(f"{graph.number_of_nodes()} Nodes in the graph: {list(graph.nodes())}")
    print(f"{graph.number_of_edges()} Edges in the graph: {list(graph.edges(data=True))}")
    for node in list(graph.nodes())[:2]:
        print(f"Neighbors of {node}: {list(graph.adj[node])}")