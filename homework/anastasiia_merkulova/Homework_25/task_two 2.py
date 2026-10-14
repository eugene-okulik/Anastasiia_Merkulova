from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def user_data():
    return {
        "first_name": "Anastasiia",
        "last_name": "Merkulova",
        "email": "anastasiia14merk@gmail.com",
        "mobile_phone": "1234567891",
        "subjects": "english",
        "current_address": "ul.obozowa120"
    }

@pytest.mark.parametrize(
    "email",
    [
        "anastasiia14merkgmail.com",
        "@gmail.com",
        "anastasiia14merk@gmail",
        "anastasiia14merk@com",
        "anastasiia14merk@@gmail.com",
        "",
        " ",
        "@##$"
    ]
)


@pytest.mark.parametrize(
    "phone_number",
    [
        "123456789",
        "1234567891",
        "12345678901",
        "abcdeftrhk",
        "!@#$#@!@#$",
        " ",
        ""
    ]
)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver

def test_fill_form(driver):
    driver.get("https://demoqa.com/automation-practice-form")


