from less_23.pages.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from less_23.pages.categories_budmat_page import Category_pick_Page
from less_23.core.locator import Locator
from less_23.locators.dashboard_locators import DashboardLocatorsCollection
from less_23.pages.login_page import LoginPage

class Dashboard(BasePage):
    def __init__(self,driver: WebDriver):
        super().__init__(driver)
        self.__nav_bar_locator = DashboardLocatorsCollection().nav_bar_locator

    def click_on_navbar(self):
        self._click(Locator(*self.__nav_bar_locator))


    def choose_subcategory(self,name):
        self._click(Locator('xpath', f"//ul[@class='catalog-menu']//a[@title='{name}']"))

        return Category_pick_Page(self._driver)

    def login_form(self):
        self._click(Locator('xpath', "//div[@class='header__login']"))
        return LoginPage(self._driver)


