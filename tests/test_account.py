import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

# Переход в ЛК
def test_personal_account_open(logged_in_driver):
    wait = WebDriverWait(logged_in_driver, 4)

    wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
    assert wait.until(EC.url_contains("/account/profile")), "Не удалось перейти в личный кабинет"

# в конструктор
def test_constructor_from_personal_account_open(logged_in_driver):

    wait = WebDriverWait(logged_in_driver, 4)

    wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(CONSTRUCTOR_BUTTON)).click()
    assert wait.until(EC.url_matches("https://stellarburgers.nomoreparties.site")), "Неверный URL после перехода"
    assert wait.until(EC.visibility_of_element_located(ORDER_BUTTON)), "Главная страница не загрузилась"

#переход через лого
def test_navigation_by_logo_from_personal_account_open(logged_in_driver):

    wait = WebDriverWait(logged_in_driver, 4)

    wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(LOGO)).click()

    assert wait.until(EC.url_matches("https://stellarburgers.nomoreparties.site")), "Неверный URL после перехода"
    assert wait.until(EC.visibility_of_element_located(ORDER_BUTTON)), "Главная страница не загрузилась"

#Выход из аккаунта через ЛК
def test_logout_from_account(logged_in_driver):

    wait = WebDriverWait(logged_in_driver, 4)

    wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()

    assert wait.until(EC.url_contains("/login")),"Не произошел переход на страницу входа после выхода, выйти не удалось"