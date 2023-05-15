from less_23.pages.base_page import BasePage
from less_23.core.locator import Locator


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_row(self, login_fill:str, password_fill:str):
        login = self._wait_until_element_appears(Locator('xpath', "//input[@id='user_login']"))
        login.send_keys(login_fill)
        password = self._wait_until_element_appears(Locator('xpath', "//input[@id='user_pass']"))
        password.send_keys(password_fill)
        self._click(Locator('xpath', "// button[ @ type = 'submit']"))






