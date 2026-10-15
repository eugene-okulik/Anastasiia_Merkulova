import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_check_added_item(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('http://testshop.qa-practice.com/')

    initial_tab = driver.current_window_handle

    product_link = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'a[href="/shop/customizable-desk-9"]')
        )
    )
    product_url = product_link.get_attribute('href')

    driver.switch_to.new_window('tab')
    driver.get(product_url)

    add_button = wait.until(
        EC.element_to_be_clickable((By.ID, 'add_to_cart'))
    )
    add_button.click()

    continue_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#modal_5 button.btn-secondary')
        )
    )
    continue_button.click()

    wait.until(
        EC.invisibility_of_element_located((By.ID, 'modal_5'))
    )
    wait.until(
        lambda d: any(
            counter.text.strip() == '1'
            for counter in d.find_elements(
                By.CSS_SELECTOR, '.my_cart_quantity'
            )
        )
    )

    driver.close()
    driver.switch_to.window(initial_tab)
    driver.get('http://testshop.qa-practice.com/shop/cart')
    cart_item = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'a[href="/shop/customizable-desk-9#attr=1,3"]')
        )
    )

    expected_text = 'Customizable Desk (Steel, White)'
    actual_text = cart_item.text.strip()
    assert expected_text == actual_text
