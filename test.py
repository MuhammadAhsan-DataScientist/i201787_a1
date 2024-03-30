import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_prediction(client):
    new_car_features = {
        'horsepower': 250,
        'enginesize': 400,
        'curbweight': 5800,
        'carwidth': 686,
        'highwaympg': 320
    }

    response = client.post('/predict', data=new_car_features, follow_redirects=True)
    assert response.status_code == 200
    assert b'Predicted Car Price' in response.data
