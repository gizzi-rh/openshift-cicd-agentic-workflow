import json
import pytest
from app import app  # Importiamo l'app Flask dal nostro file app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_data(client):
    response = client.get('/api/data')  # Inviamo una richiesta GET all'endpoint
    assert response.status_code == 200  # Verifichiamo che il codice di stato sia 200 (OK)
    
    data = json.loads(response.data)  # Carichiamo la risposta JSON
    assert 'message' in data  # Verifichiamo che ci sia una chiave 'message' nella risposta
