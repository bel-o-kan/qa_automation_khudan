class DashboardLocatorsCollection():
    def __init__(self):
        self.__nav_bar_locator = ('xpath', "//div[@class='header__burger']")


    @property
    def nav_bar_locator(self):
        return self.__nav_bar_locator


