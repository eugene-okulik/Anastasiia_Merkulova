import allure

import pytest


VALID_DATA = {
    "name": "Anastasiia",
    "data": {
        "data": {
            "test_one": "test_one"
        }
    }
}, {
    "name": "Mark",
    "data": {
        "data": {
            "test_two": "test_two"
        }
    }
}, {
    "name": "Anton",
    "data": {
        "data": {
            "test_three": "test_three"}
    }
}

INVALID_DATA = (
    {
        "name": 123},
    {
        "data": {
            "data": {}
        }
    }
)


@allure.feature('Posts')
@allure.story('Create post with valid data')
@allure.title('Check response for creating a post with valid data')
@pytest.mark.critical
@pytest.mark.parametrize("data", VALID_DATA)
def test_create_post(create_post_endpoint, data):
    create_post_endpoint.new_post(body=data)
    with allure.step('Create a new post'):
        assert create_post_endpoint.response.status_code == 200
        assert create_post_endpoint.json['name'] == data['name']
        assert create_post_endpoint.json['data'] == data['data']
        assert isinstance(create_post_endpoint.json['id'], int)


@allure.feature('Posts')
@allure.story('Create post with invalid data')
@allure.title('Check response for creating a post with invalid data')
@pytest.mark.high
@pytest.mark.parametrize("data", INVALID_DATA)
def test_create_post_invalid_data(create_post_endpoint, data):
    print("\nDATA:", data)
    create_post_endpoint.new_post(body=data)
    print("STATUS:", create_post_endpoint.response.status_code)
    with allure.step('Create a new post with invalid data'):
        assert create_post_endpoint.response.status_code == 400
        assert "id" not in create_post_endpoint.json


@allure.feature('Posts')
@allure.story('Get all posts')
@allure.title('Check response for getting all posts')
@pytest.mark.critical
def test_get_all_posts(get_post_endpoint, created_post):
    get_post_endpoint.get_posts()
    with allure.step('Get all posts'):
        assert get_post_endpoint.response.status_code == 200
        assert len(get_post_endpoint.json) > 0


@allure.feature('Posts')
@allure.story('Get one post')
@allure.title('Check response for getting one post')
@pytest.mark.critical
def test_get_one_post(get_one_post_endpoint,created_post):
    get_one_post_endpoint.get_one_post(created_post)
    with allure.step('Get one post by id'):
        assert get_one_post_endpoint.response.status_code == 200
        assert get_one_post_endpoint.json["id"] == created_post


@allure.feature('Posts')
@allure.story('Update a post')
@allure.title('Check response for updating the post')
@pytest.mark.critical
def test_put_a_post(put_post_endpoint, created_post):
    data = {
        "name": "Anna",
        "data": {
        "data": "test_four"}
    }
    put_post_endpoint.update_a_post(data, created_post)
    with allure.step('Update a post'):
        assert put_post_endpoint.response.status_code == 200
        assert put_post_endpoint.json['name'] == data["name"]


@allure.feature('Posts')
@allure.story('Partially update')
@allure.title('Checking response for updating a post partially')
@pytest.mark.critical
@pytest.mark.critical
def test_patch_a_post(patch_post_endpoint, created_post):
    data = {
        "name": "new_test_one"
    }
    patch_post_endpoint.update_a_part_of_post(data, created_post)
    with allure.step('Partually update a post'):
        assert patch_post_endpoint.response.status_code == 200
        assert patch_post_endpoint.json['name'] == data["name"]


@allure.feature('Posts')
@allure.story('Delete a post')
@allure.title('Checking response for deleting a post')
@pytest.mark.critical
def test_delete_a_post(delete_post_endpoint, created_post):
    delete_post_endpoint.delete_a_post(created_post)
    with allure.step('Delete a post'):
        assert delete_post_endpoint.response.status_code == 200
