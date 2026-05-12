import requests

import pytest

@pytest.fixture(scope='session', autouse=True)
def write_start_test():
    print('Start test')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def before_test():
    print('Before test')


@pytest.fixture(autouse=True)
def after_test():
    print('After test')


@pytest.fixture
def post_id():
    create_id = create_new_post()
    yield create_id
    clear(create_id)


def create_new_post():
        body = {
            "name": "test",
            "data": {
                "test": "test"
            }
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'http://objapi.course.qa-practice.com/object',
            json=body,
            headers=headers
        )
        return response.json()['id']


def clear(post_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    assert response.status_code in [200, 204, 404], 'Delete failed'


def test_all_posts():
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    assert len(response) == 1, 'Not all posts returned'


def test_one_post(post_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{post_id}').json()
    assert response['id'] == post_id


@pytest.mark.parametrize(
    "body",
    [
        {"name": "test_1", "data": {"test": "one"}},
        {"name": "test_2", "data": {"test": "two"}},
        {"name": "test_3", "data": {"test": "three"}},
    ]
)
@pytest.mark.critical
def test_create_post(body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()['name'] == body['name']
    clear(response.json()['id'])


def test_put_a_post(post_id):
    body = {
        "name": "new_test",
        "data": {
            "test": "new_test"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == "new_test"

@pytest.mark.medium
def test_patch_a_post(post_id):
    body = {
        "name": "new_test_one"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == "new_test_one"


def test_delete_a_post(post_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    assert response.status_code in [200, 204], 'Delete failed'


test_all_posts()
