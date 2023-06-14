from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cookies:
    def __init__(self, driver):
        self.driver = driver

    def get_cookies(self):
        cookies = self.driver.get_cookies()
        return cookies

    def set_cookies(self, cookies):
        for cookie in cookies:
            self.driver.add_cookie(cookie)


class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def get_item(self, key):
        value = self.driver.execute_script(f"return window.localStorage.getItem('{key}');")
        return value

    def set_item(self, key, value):
        self.driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")

    def remove_item(self, key):
        self.driver.execute_script(f"window.localStorage.removeItem('{key}');")


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.cookies = Cookies(driver)
        self.local_storage = LocalStorage(driver)


# Запуск веб-драйвера
options = Options()
# options.add_argument("--headless")  # Запуск у безголовому режимі (фоновий режим)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Відкриття сторінки Rozetka
driver.get("https://rozetka.com.ua/")

# Ініціалізація базової сторінки
base_page = BasePage(driver)

# Логін на сайт
login_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//rz-user/button[@type='button']"))
)
login_link.click()

email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='auth_email']"))
)
email_input.send_keys("0980911380")

password_input = driver.find_element(By.XPATH, "//input[@id='auth_pass']")
password_input.send_keys("2301ZydfhZ198")


login_button = driver.find_element(By.XPATH, "//button[@class='button button--large button--green auth-modal__submit ng-star-inserted']")
login_button.click()
#
'''Будемо вважати, що пройшли reCAPTCHA'''
# captcha_check = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@id='recaptcha-anchor']//div[@class='recaptcha-checkbox-checkmark']")))
# captcha_check.click()
# login_button.click()

# Повернення на головну сторінку
home_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div//a[@class='header__logo']")))
home_link.click()

# Приклад використання методів Cookies та LocalStorage
cookies = base_page.cookies.get_cookies()
print(cookies)

local_storage_value = base_page.local_storage.get_item("example_key")
print(local_storage_value)

# Закриття браузера
driver.quit()
