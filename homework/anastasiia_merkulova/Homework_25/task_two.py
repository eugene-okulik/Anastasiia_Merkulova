from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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


def test_full_element_fields(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    field_name = driver.find_element(By.ID, 'firstName')
    field_name.send_keys('Anastasiia')
    field_last_name = driver.find_element(By.ID, 'lastName')
    field_last_name.send_keys('Merkulova')
    field_email = driver.find_element(By.ID, 'userEmail')
    field_email.send_keys('anastasiia14@gmail.com')
    gender_button = driver.find_element(By.ID, 'gender-radio-2')
    gender_button.click()
    fild_mobile = driver.find_element(By.ID, 'userNumber')
    fild_mobile.send_keys('1234567891')
    date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth.click()
    month = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select')
    month = Select(month)
    month.select_by_visible_text('August')
    year = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select')
    year = Select(year)
    year.select_by_visible_text('1994')
    day = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day--014')
    day.click()
    subjects_field = driver.find_element(By.ID, 'subjectsInput')
    subjects_field.send_keys('Eng')
    english_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'subjects-auto-complete__option') "
                "and text()='English']"
            )
        )
    )
    english_option.click()
    field_hobbies = driver.find_element(By.ID, 'hobbies-checkbox-1')
    field_hobbies.click()
    current_adress_field = driver.find_element(By.ID, 'currentAddress')
    current_adress_field.send_keys('New York')

    state_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, 'react-select-3-input')
        )
    )

    driver.execute_script(
        """
        const footer = document.querySelector('footer');
        if (footer) {
            footer.style.display = 'none';
        }

        const banner = document.getElementById('fixedban');
        if (banner) {
            banner.style.display = 'none';
        }

        arguments[0].scrollIntoView({block: 'center'});
        """,
        state_input
    )

    state_input.send_keys('Haryana')
    state_input.send_keys(Keys.ENTER)

    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, 'submit')
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        submit_button
    )

    driver.execute_script(
        "arguments[0].click();",
        submit_button
    )


    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, 'submit')
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        submit_button
    )
