import json
from jsonschema import validate
import requests
from pathlib import Path
from schemas.users import user, create, update


def test_all_the_users_should_have_unique_id():
    response = requests.get('https://reqres.in/api/users')
    body = response.json()
    ids = [element['id'] for element in body['data']]

    assert response.status_code == 200
    assert body['total'] == 12
    assert list(set(ids)) == ids
    with open(Path(__file__).parent.parent.joinpath(f'schemas/users.json')) as file:
        validate(body, schema=json.loads(file.read()))


def test_get_user_by_id():
    id = '2'

    response = requests.get('https://reqres.in/api/users/' + id)
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=user)


def test_get_non_existent_user_by_id():
    id = '23'
    response = requests.get('https://reqres.in/api/users/' + id)
    body = response.json()

    assert response.status_code == 404
    assert body == {}


def test_create_user():
    name = 'Vasya'
    job = 'dvornik'

    payload = {'name': name, 'job': job}
    response = requests.post('https://reqres.in/api/users', json=payload)
    body = response.json()

    assert response.status_code == 201
    assert body['name'] == name
    assert body['job'] == job
    validate(body, schema=create)


def test_update_user_info():
    name = 'Igor'
    job = 'driver'
    id = '2'

    payload = {'name': name, 'job': job}
    response = requests.put('https://reqres.in/api/users/' + id, json=payload)
    body = response.json()

    assert response.status_code == 200
    assert body['name'] == name
    assert body['job'] == job
    validate(body, schema=update)


def test_delete_user():
    id = '2'
    response = requests.delete('https://reqres.in/api/users/' + id)

    assert response.status_code == 204


def test_users_per_page_should_have_correct_count():
    response = requests.get('https://reqres.in/api/users')
    body = response.json()
    ids = [element['id'] for element in body['data']]

    assert response.status_code == 200
    assert len(ids) == body['per_page']
    with open(Path(__file__).parent.parent.joinpath(f'schemas/users.json')) as file:
        validate(body, schema=json.loads(file.read()))
