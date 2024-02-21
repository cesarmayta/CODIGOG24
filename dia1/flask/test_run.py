import pytest
from run import app,db,Tarea

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

class TestTareaEndpoints:
    def test_set_tarea(self,client):
        tarea_data = {
            'descripcion': 'tarea 1',
            'estado':'pendiente'
        }
        response = client.post('/tarea',json=tarea_data)
        assert response.status_code == 200
        assert b'tarea 1' in response.data

    def test_get_tarea(self,client):
        tarea = Tarea(descripcion='tarea 1',estado = 'pendiente')
        db.session.add(tarea)
        db.session.commit()

        response = client.get('/tarea')
        assert response.status_code == 200
        assert b'tarea 1' in response.data

    def test_get_tarea_id(self,client):
        tarea = Tarea(descripcion='tarea 1',estado='pendiente')
        db.session.add(tarea)
        db.session.commit()

        response = client.get(f'/tarea/{tarea.id}')
        assert response.status_code == 200
        assert b'tarea 1' in response.data
