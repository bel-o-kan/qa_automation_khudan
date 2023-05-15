from less_23.pages.base_page import BasePage
from less_23.pages.building_materials_subcategory_l2_page import BuildingMaterialL2Page
from less_23.core.locator import Locator

class Category_pick_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__building_materials_locator = Locator('xpath', "//div[@class='shop-categories__container']//a[@class='shop-category__picture']/following-sibling::a[contains(text(),'Будівельні матеріали')]")


    def choose_building_materials_section(self):
        self._click(self.__building_materials_locator)
        return BuildingMaterialL2Page(self._driver)