import pytest
from app import app

@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_user_role(test_client):
    response = test_client.get('/api/user/5/role')
    assert response.status_code == 200
    data = response.get_json()
    assert 'role_description' in data

def test_create_user(test_client):
    user_data = {
        'name': 'Rachel',
        'email': 'oyugi@gmail.com',
        'password': '567yffttyyu',
        'role_id': 5
    }
    response = test_client.post('/api/user', json=user_data)
    assert response.status_code == 201


if __name__ == '__main__':
    pytest.main()