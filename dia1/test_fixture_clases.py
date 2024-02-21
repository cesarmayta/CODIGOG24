import pytest

@pytest.fixture
def setup_data():
    data = {
        'nombre':'Cesar',
        'email':'cesar@gmail.com'
    }
    return data

class TestExample:
    def test_name(self,setup_data):
        assert setup_data['nombre'] == 'Cesar'

    def test_email(self,setup_data):
        assert setup_data['email'] == 'cesar@gmail.com'