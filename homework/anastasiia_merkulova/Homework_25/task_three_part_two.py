from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_show_text(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button = driver.find_element(By.CSS_SELECTOR, '#start button')
    button.click()
    text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'finish'))
    )
    assert text.text == 'Hello World!'
