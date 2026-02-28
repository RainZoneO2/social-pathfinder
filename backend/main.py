from core.graph_engine import ( build_demo_graph, assign_edge_weights, print_graph_info)
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

def main():
    graph = build_demo_graph()
    assign_edge_weights(graph)
    print_graph_info(graph)

if __name__ == "__main__":
    main()