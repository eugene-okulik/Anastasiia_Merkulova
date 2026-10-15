import pytest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_check_click(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('http://testshop.qa-practice.com/')

    product_card = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#products_grid form.oe_product_cart')
        )
    )
    expected_name = product_card.find_element(
        By.CSS_SELECTOR, 'a[itemprop="name"]'
    ).text.strip()

    product_image = product_card.find_element(By.CSS_SELECTOR, 'img')
    ActionChains(driver).move_to_element(product_image).perform()

    shopping_cart = wait.until(
        EC.element_to_be_clickable(
            product_card.find_element(
                By.CSS_SELECTOR, 'a[aria-label="Shopping cart"]'
            )
        )
    )
    shopping_cart.click()

    popup_item = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.modal.show .main_product .product_display_name')
        )
    )
    actual_name = popup_item.text.strip()

    assert expected_name in actual_name, (
        f'Ожидали товар {expected_name!r}, получили {actual_name!r}'
    )
