from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_find_element(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    search_input = driver.find_element(By.ID, "id_text_string")
    search_input.send_keys("Buttons")
    search_input.send_keys(Keys.ENTER)
    result = WebDriverWait(driver,10) .until(EC.visibility_of_element_located((By.ID, "result-text")))
    print(result.text)
    assert result.text == "Buttons"
