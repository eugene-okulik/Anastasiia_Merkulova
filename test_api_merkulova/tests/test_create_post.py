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
def test_create_object(create_object_endpoint, data):
    create_object_endpoint.new_object(body=data)
    with allure.step('Create a new post'):
        create_object_endpoint.check_status_code(200)
        assert create_object_endpoint.json['name'] == data['name']
        assert create_object_endpoint.json['data'] == data['data']
        assert isinstance(create_object_endpoint.json['id'], int)


@allure.feature('Posts')
@allure.story('Create post with invalid data')
@allure.title('Check response for creating a post with invalid data')
@pytest.mark.high
@pytest.mark.parametrize("data", INVALID_DATA)
def test_create_object_invalid_data(create_object_endpoint, data):
    print("\nDATA:", data)
    create_object_endpoint.new_object(body=data)
    print("STATUS:", create_object_endpoint.response.status_code)
    with allure.step('Create a new post with invalid data'):
        create_object_endpoint.check_status_code(400)
        assert "id" not in create_object_endpoint.json


@allure.feature('Posts')
@allure.story('Get all posts')
@allure.title('Check response for getting all posts')
@pytest.mark.critical
def test_get_all_objects(get_objects_endpoint, created_object):
    get_objects_endpoint.get_objects()
    with allure.step('Get all posts'):
        get_objects_endpoint.check_status_code(200)
        assert len(get_objects_endpoint.json) > 0


@allure.feature('Posts')
@allure.story('Get one post')
@allure.title('Check response for getting one post')
@pytest.mark.critical
def test_get_one_object(get_one_object_endpoint, created_object):
    get_one_object_endpoint.get_one_object(created_object)
    with allure.step('Get one post by id'):
        get_one_object_endpoint.check_status_code(200)
        assert get_one_object_endpoint.json["id"] == created_object


@allure.feature('Posts')
@allure.story('Update a post')
@allure.title('Check response for updating the post')
@pytest.mark.critical
def test_put_object(put_object_endpoint, created_object):
    data = {
        "name": "Anna",
        "data": {
            "data": "test_four"
        }
    }
    put_object_endpoint.update_object(data, created_object)
    with allure.step('Update a post'):
        put_object_endpoint.check_status_code(200)
        assert put_object_endpoint.json['name'] == data["name"]


@allure.feature('Posts')
@allure.story('Partially update')
@allure.title('Checking response for updating a post partially')
@pytest.mark.critical
@pytest.mark.critical
def test_patch_object(patch_object_endpoint, created_object):
    data = {
        "name": "new_test_one"
    }
    patch_object_endpoint.update_a_part_of_object(data, created_object)
    with allure.step('Partually update a post'):
        patch_object_endpoint.check_status_code(200)
        assert patch_object_endpoint.json['name'] == data["name"]


@allure.feature('Posts')
@allure.story('Delete a post')
@allure.title('Checking response for deleting a post')
@pytest.mark.critical
def test_delete_a_post(delete_object_endpoint, created_object):
    delete_object_endpoint.delete_object(created_object)
    with allure.step('Delete a post'):
        delete_object_endpoint.check_status_code(200)
