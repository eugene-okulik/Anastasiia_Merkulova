import requests
import pytest
import allure


@pytest.fixture(scope='session', autouse=True)
def write_start_test():
    print('Start test')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def before_test():
    print('Before test')
    yield
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


@allure.feature('Post')
@allure.story('Clear')
@allure.title('Delete exiting post')
def clear(post_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    with allure.step('Delete exiting post'):
        assert response.status_code in [200, 204, 404], 'Delete failed'



@allure.feature('Posts')
@allure.story('Get')
@allure.title('Get all posts')
def test_all_posts():
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    with allure.step('Get all posts'):
        assert len(response) == 1, 'Not all posts returned'

@allure.feature('Posts')
@allure.story('Get')
@allure.title('Get one post by id')
def test_one_post(post_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{post_id}').json()
    with allure.step('Get one post by id'):
        assert response['id'] == post_id


@pytest.mark.parametrize(
    "body",
    [
        {"name": "test_1", "data": {"test": "one"}},
        {"name": "test_2", "data": {"test": "two"}},
        {"name": "test_3", "data": {"test": "three"}},
    ]
)


@allure.feature('Posts')
@allure.story('Create')
@allure.title('Create a new post with valid data')
@pytest.mark.critical
def test_create_post(body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    with allure.step('Create a new post'):
        assert response.status_code == 200
        assert response.json()['name'] == body['name']
        clear(response.json()['id'])


@allure.feature('Posts')
@allure.story('Update')
@allure.title('Update a post')
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
    with allure.step('Update a post'):
        assert response['name'] == "new_test"


@allure.feature('Posts')
@allure.story('Update')
@allure.title('Update a part of a post')
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
    with allure.step('Update a part of a post'):
        assert response['name'] == "new_test_one"


@allure.feature('Posts')
@allure.story('Delete')
@allure.title('Delete a post')
def test_delete_a_post(post_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    with allure.step('Delete a post'):
        assert response.status_code in [200, 204], 'Delete failed'
