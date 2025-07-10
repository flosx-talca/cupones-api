from app.api import app
def test_success():
    client = app.test_client()
    response = client.post('/price', json={"price": 990, "cupon": "SALES10"})
    assert response.status_code == 200


def test_failure():
    client = app.test_client()
    response = client.post('/price', json={"price": "990", "cupon": "SALES10"})
    assert response.status_code == 500
  
