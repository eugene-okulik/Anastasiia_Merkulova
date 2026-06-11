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
            "test_two" : "test_two"
        }
    }
}, {
    "name": "Anton",
    "data": {
        "data": {
            "test_three" : "test_three"        }
    }
}

INVALID_DATA = (
    {
        "name": 123
},
    {
        "data": {
            "data": {}
        }
    }
)

@allure.feature('Posts')
@allure.story('Create post with valid data')
@allure.title('Check response for valid data')
@pytest.mark.critical
@pytest.mark.parametrize("data", VALID_DATA)
def test_create_post(create_post_endpoint, data):
    create_post_endpoint.new_post(body=data)
    with allure.step('Create a new post'):
        assert create_post_endpoint.response.status_code == 200
        assert create_post_endpoint.json['name'] == data['name']
        assert create_post_endpoint.json['data'] == data['data']
        assert isinstance (create_post_endpoint.json['id'], int)


@allure.feature('Posts')
@allure.story('Create post with invalid data')
@allure.title('Check response for invalid data')
@pytest.mark.high
@pytest.mark.parametrize("data", INVALID_DATA )
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
def test_get_all_posts(get_post_endpoint):
    get_post_endpoint.get_posts()
    with allure.step('Get all posts'):
        assert get_post_endpoint.response.status_code == 200
        assert len(get_post_endpoint.json) > 0


@allure.feature('Posts')
@allure.story('Get one post')
@allure.title('Get one post by id')
@pytest.mark.critical
def test_one_post(get_post_endpoint,data):
    get_post_endpoint.get_posts()
    with allure.step('Get one post by id'):
        assert get_post_endpoint.response.status_code == 200
        assert get_post_endpoint.json['id'] == data['id']
        assert isinstance (get_post_endpoint.json['id'], int)
