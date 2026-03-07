from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_get_demo_graph():
    response = client.get("/demo-graph")
    assert response.status_code == 200
    
    data = response.json()

    assert 'nodes' in data
    assert 'edges' in data

    assert isinstance(data['nodes'], list)
    assert isinstance(data['edges'], list)

    assert len(data['nodes']) > 0
    assert len(data['edges']) > 0