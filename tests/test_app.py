from fastapi.testclient import TestClient


def test_root_deve_retornar_200_e_hello_world(client: TestClient):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, World!'}


def test_create_user(client: TestClient):
    response = client.post(
        '/users/',
        json={
            'username': 'roberto',
            'email': 'roberto@teste.com',
            'password': 'teste$123',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'username': 'roberto',
        'email': 'roberto@teste.com',
        'id': 1,
    }


def test_get_users(client: TestClient):
    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {'id': 1, 'username': 'roberto', 'email': 'roberto@teste.com'}
        ]
    }


def test_update_user(client: TestClient):
    response = client.put(
        '/users/1',
        json={
            'username': 'name updated',
            'email': 'email@updated.com',
            'password': 'password_updated',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'username': 'name updated',
        'email': 'email@updated.com',
    }


def test_delete_user(client: TestClient):
    response = client.delete('users/1')

    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}
