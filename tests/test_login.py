from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import *

class TestLogin:
    #Вход через кнопку на главной
    def test_login_via_main_button(self, driver, wait):

        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()
        wait.until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT))
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(STABLE_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(STABLE_PASS)
        driver.find_element(*LOGIN_BUTTON).click()

        assert wait.until(EC.visibility_of_element_located(ORDER_BUTTON)), "Кнопка 'Оформить заказ' не отображается"

    #Вход через кнопку Личный кабинет
    def test_login_via_personal_account(self, driver, wait):

        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT))
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(STABLE_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(STABLE_PASS)
        driver.find_element(*LOGIN_BUTTON).click()

        assert wait.until(EC.visibility_of_element_located(ORDER_BUTTON)), "Кнопка 'Оформить заказ' не отображается"

    #Вход через кнопку в форме регистрации
    def test_login_via_register_form(self, driver, wait):

        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()
        wait.until(EC.element_to_be_clickable(REGISTER_LINK)).click()
        wait.until(EC.element_to_be_clickable(REGISTER_LOGIN_LINK)).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(STABLE_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(STABLE_PASS)
        driver.find_element(*LOGIN_BUTTON).click()

        assert wait.until(EC.visibility_of_element_located(ORDER_BUTTON)), "Кнопка 'Оформить заказ' не отображается"

    #Вход через кнопку в форме восстановления пароля
    def test_login_via_password_recovery(self, driver, wait):

        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()
        wait.until(EC.element_to_be_clickable(RECOVERY_LINK)).click()
        wait.until(EC.element_to_be_clickable(RECOVERY_LOGIN_LINK)).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(STABLE_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(STABLE_PASS)
        driver.find_element(*LOGIN_BUTTON).click()

        assert wait.until(EC.visibility_of_element_located(ORDER_BUTTON)), "Кнопка 'Оформить заказ' не отображается"
