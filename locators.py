from selenium.webdriver.common.by import By

LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") # лого

# Главная страница
LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]") # кнопка войти в аккаунт
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href='/account']//p[text()='Личный Кабинет']") # кнопка личный кабинет
CONSTRUCTOR_BUTTON = (By.XPATH, ".//a[@href='/']//p[text()='Конструктор']") # кнопка конструктор
ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]") # кнопка оформить заказ, после авторизации

# Форма регистрации
NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input") # поле ввода имени
EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input") # поле ввода почты
PASSWORD_INPUT = (By.XPATH, "//input[@type='password']") # поле ввода пароля
REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]") # кнопка зарегистрироваться
PASSWORD_ERROR = (By.CSS_SELECTOR, ".input__error.text_type_main-default") # текст ошибки неверного пароля
REGISTER_LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]") # переход на форму авторизации из формы регистрации

# Форма входа
REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]") # переход на форму регистрации из формы авторизации
LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@type='text']") # поле ввода почты
LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']") # поле ввода пароля
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # кнопка авторизации
RECOVERY_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]") # переход на форму восстановления из формы авторизации

#Форма восстановления
RECOVERY_LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]") # переход на форму авторизации из формы восстановления

# Личный кабинет
LOGOUT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Выход')]") #кнопка выхода из УЗ в ЛК

# Конструктор
BUNS_TAB = (By.XPATH, "//div[./span[text()='Булки']]") # раздел с булками
SAUCES_TAB = (By.XPATH, "//div[./span[text()='Соусы']]") # раздел с соусами
TOPPINGS_TAB = (By.XPATH, "//div[./span[text()='Начинки']]") # раздел с начинками
ACTIVE_TAB = (By.CSS_SELECTOR, "div.tab_tab_type_current__2BEPc") # активный раздел