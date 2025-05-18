import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import *
from urls import *

#Фикстура для инициализации драйвера
@pytest.fixture
def driver():
    #убран хардкод пути до драйвера
    driver = webdriver.Chrome()
    driver.get(MAIN_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

#Фикстура готовой авторизации для проверки переходов в ЛК и из ЛК в test_account.py
@pytest.fixture
def logged_in_driver(driver):
    wait = WebDriverWait(driver, 4)

    # Авторизация
    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()
    wait.until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)).send_keys(STABLE_EMAIL)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(STABLE_PASS)
    driver.find_element(*LOGIN_BUTTON).click()

    # Ожидание входа
    wait.until(EC.visibility_of_element_located(ORDER_BUTTON))
    return driver

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 4)
