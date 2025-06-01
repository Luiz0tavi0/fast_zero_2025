from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')

    assert response.json() == {'message': 'Hello, World!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testeusername',
            'password': 'testepassword',
            'email': 'test@gmail.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testeusername',
        'id': 1,
        'email': 'test@gmail.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testeusername',
                'id': 1,
                'email': 'test@gmail.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'novousername',
            'password': 'trocadopassword',
            'email': 'trocado@gmail.com',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'novousername',
        'email': 'trocado@gmail.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    response.json() == {'message': 'User deleted'}


def test_deve_lancar_not_found_ao_atualizar(client):
    response = client.put(
        '/users/0',
        json={
            'username': 'novousername',
            'password': 'trocadopassword',
            'email': 'trocado@gmail.com',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_deve_lancar_not_found_ao_deletar(client):
    response = client.delete('/users/0')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
