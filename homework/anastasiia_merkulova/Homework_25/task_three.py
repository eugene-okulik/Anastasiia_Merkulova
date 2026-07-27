from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_choose_language(driver):
    language = 'Python'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select_language = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'id_choose_language'))
    )
    select_language = Select(select_language)
    select_language.select_by_visible_text('Python')
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()
    result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'result'))
    )
    assert result.text == f'You selected\n{language}'
