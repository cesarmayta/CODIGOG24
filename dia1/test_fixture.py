import pytest

@pytest.fixture
def setup_data():
    data = {
        'nombre':'Cesar',
        'email':'cesar@gmail.com'
    }
    return data

def test_example(setup_data):
    assert setup_data['nombre'] == 'Cesar'
    assert setup_data['email'] == 'cesar@gmail.com'

    