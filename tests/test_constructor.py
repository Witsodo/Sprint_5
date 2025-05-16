import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


def test_buns_section(driver):
    wait = WebDriverWait(driver, 4)

    # Проверка начального состояния - активны "Булки"
    wait.until(EC.visibility_of_element_located(BUNS_TAB))
    active_tab = wait.until(EC.visibility_of_element_located(ACTIVE_TAB))
    assert "Булки" in active_tab.text, "По умолчанию должна быть активна вкладка 'Булки'"

    # Переход на "Соусы"
    sauces_tab = driver.find_element(*SAUCES_TAB)
    sauces_tab.click()
    #явное ожидания для корректной прогрузки  переключения
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(ACTIVE_TAB, "Соусы"))

    # Возврат на "Булки"
    buns_tab = driver.find_element(*BUNS_TAB)
    buns_tab.click()
    # Явное ожидание смены активной вкладки
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(ACTIVE_TAB, "Булки"))
    active_tab = wait.until(EC.visibility_of_element_located(ACTIVE_TAB))
    assert "Булки" in active_tab.text, "После возврата должна снова быть активна вкладка 'Булки'"

def test_sauces_section(driver):
    wait = WebDriverWait(driver, 4)

    sauces_tab = driver.find_element(*SAUCES_TAB)
    sauces_tab.click()
    WebDriverWait(driver, 0.5)

    active_tab = wait.until(EC.visibility_of_element_located(ACTIVE_TAB))

    assert "Соусы" in active_tab.text, "Должна быть активна вкладка 'Соусы'"

def test_toppings_section(driver):
    wait = WebDriverWait(driver, 4)

    toppings_tab = driver.find_element(*TOPPINGS_TAB)
    toppings_tab.click()
    WebDriverWait(driver, 0.5)
    active_tab = wait.until(EC.visibility_of_element_located(ACTIVE_TAB))
    assert "Начинки" in active_tab.text, "Должна быть активна вкладка 'Начинки'"