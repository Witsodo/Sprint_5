from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from util.generators import generate_email, generate_password

#Успешная регистрация
def test_successful_registration(driver):
    wait = WebDriverWait(driver, 4)
    # Переход на страницу регистрации
    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()
    wait.until(EC.element_to_be_clickable(REGISTER_LINK)).click()
    # Ожидание загрузки формы
    wait.until(EC.visibility_of_element_located(NAME_INPUT))
    # Заполнение формы
    driver.find_element(*NAME_INPUT).send_keys("Михаил")
    driver.find_element(*EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*PASSWORD_INPUT).send_keys(generate_password(6))

    # Клик по кнопке регистрации
    wait.until(EC.element_to_be_clickable(REGISTER_BUTTON)).click()
    # Проверка успешной регистрации
    assert wait.until(EC.url_contains("/login")), "Не произошёл переход на страницу входа после регистрации"

#ошибка при невалидном пароле
def test_invalid_password_error(driver):
    wait = WebDriverWait(driver, 4)
    # Переход на регистрацию
    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()
    wait.until(EC.element_to_be_clickable(REGISTER_LINK)).click()
    wait.until(EC.visibility_of_element_located(NAME_INPUT))
    # Заполнение формы с некорректным паролем
    driver.find_element(*NAME_INPUT).send_keys("Михаил")
    driver.find_element(*EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*PASSWORD_INPUT).send_keys("123")  # Слишком короткий пароль
    driver.find_element(*REGISTER_BUTTON).click()

    # Проверка сообщения об ошибке
    error = wait.until(EC.visibility_of_element_located(PASSWORD_ERROR))
    assert "Некорректный пароль" in error.text, "Не отображается сообщение об ошибке пароля"