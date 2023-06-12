from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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
options.add_argument("--headless")  # Запуск у безголовому режимі (фоновий режим)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Відкриття сторінки Rozetka
driver.get("https://rozetka.com.ua/")

# Ініціалізація базової сторінки
base_page = BasePage(driver)

# Приклад використання методів Cookies та LocalStorage
cookies = base_page.cookies.get_cookies()
print(cookies)

local_storage_value = base_page.local_storage.get_item("example_key")
print(local_storage_value)

# Закриття браузера
driver.quit()
