import pytest
from m import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_math(client):
    response = client.get('/math/5')
    assert response.status_code == 200
    print(response.data.decode('utf-8'))

def test_second(client):
    response = client.get('/second')
    assert response.status_code == 200
    print(response.data.decode('utf-8'))


def test_number(client):
    number = 20
    response = client.get(f'/number/{number}')
    assert response.status_code == 200
    assert f"result: {number * 2}" == response.data.decode('utf-8')
    print(response.data.decode('utf-8'))
