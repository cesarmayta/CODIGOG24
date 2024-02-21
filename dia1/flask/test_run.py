import pytest
from run import app,db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client

    with app.app_context():
        db.drop_all()


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'prueba flask' in response.data