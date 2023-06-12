from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options


def test_search_lego_duplo():
    options = Options()
    driver = Chrome(options=options)
    driver.get('https://rozetka.com.ua/')
    wait = WebDriverWait(driver, 5)
    menu = "//button[text()=' Каталог ']"
    navigate_menu = wait.until(EC.visibility_of_element_located(('xpath', menu)))
    navigate_menu.click()
    categorie = "(//a[text()='Товари для геймерів'])[2]"
    categorie_menu = wait.until(EC.visibility_of_element_located(('xpath', categorie)))
    categorie_menu.click()
    time.sleep(5)
    driver.quit()


def test_add_ps5_digit_ed():
    """додавання товара в корзину"""
    options = Options()
    driver = Chrome(options=options)
    driver.get('https://rozetka.com.ua/')
    wait = WebDriverWait(driver, 5)
    menu = "//button[text()=' Каталог ']"
    categorie = "(//a[text()='Товари для геймерів'])[2]"
    consoles_link = "//a/img[@alt='Ігрові приставки']"
    add_button = "//div[contains(@class, 'goods-tile__inner')]//a[contains(@title, 'Ігрова приставка PS5 PlayStation " \
                 "5')]/ancestor::div[@class='goods-tile__inner']//button[@aria-label='Купити']"
    navigate_menu = wait.until(EC.visibility_of_element_located(('xpath', menu)))
    navigate_menu.click()

    categorie_menu = wait.until(EC.visibility_of_element_located(('xpath', categorie)))
    categorie_menu.click()

    consoles = wait.until(EC.visibility_of_element_located(('xpath', consoles_link)))
    consoles.click()

    time.sleep(1)
    add_to_basket = driver.find_element(by='xpath', value=add_button)
    add_to_basket.click()

    time.sleep(5)
    driver.quit()


def test_check_basket():
    """перевірка, що товар додано в корзину"""
    options = Options()
    driver = Chrome(options=options)
    driver.get('https://rozetka.com.ua/')
    wait = WebDriverWait(driver , 5)
    header_logo = "//div//a[@class='header__logo']"
    menu = "//button[text()=' Каталог ']"
    categorie = "(//a[text()='Товари для геймерів'])[2]"
    consoles_link = "//a/img[@alt='Ігрові приставки']"
    add_button = "//div[contains(@class, 'goods-tile__inner')]//a[contains(@title, 'Ігрова приставка PS5 PlayStation " \
                 "5')]/ancestor::div[@class='goods-tile__inner']//button[@aria-label='Купити']"
    basket_button = "//li[@class='header-actions__item header-actions__item--cart']"
    goods_header = "//a[@class='cart-product__title'][@title='Ігрова приставка PS5 PlayStation 5']"

    navigate_menu = wait.until(EC.visibility_of_element_located(('xpath' , menu)))
    navigate_menu.click()

    categorie_menu = wait.until(EC.visibility_of_element_located(('xpath' , categorie)))
    categorie_menu.click()

    consoles = wait.until(EC.visibility_of_element_located(('xpath' , consoles_link)))
    consoles.click()

    time.sleep(2)
    add_to_basket = driver.find_element(by='xpath' , value=add_button)
    add_to_basket.click()

    time.sleep(3)
    main_page = driver.find_element(by='xpath' , value=header_logo)
    main_page.click()

    basket = driver.find_element(by='xpath' , value=basket_button)
    basket.click()

    goods = wait.until(EC.visibility_of_element_located(('xpath' , goods_header)))
    assert goods.text == "Ігрова приставка PS5 PlayStation 5" , "Товар не знайдений у корзині"

    driver.quit()


def test_points_of_delivery_present():
    options = Options()
    driver = Chrome(options=options)
    driver.get('https://rozetka.com.ua/')
    wait = WebDriverWait(driver , 5)
    points_of_delivery_link = "(//a[@class ='button button--medium button--with-icon main-links__help " \
                              "ng-star-inserted'])[2]"
    point_adress = "//p[text()=' вул. Олени Теліги, 25 ']"

    points_of_delivery_list = wait.until(EC.visibility_of_element_located(('xpath', points_of_delivery_link)))
    points_of_delivery_list.click()

    check_point_present = wait.until(EC.visibility_of_element_located(('xpath', point_adress)))
    assert check_point_present.text == "вул. Олени Теліги, 25", "point not present"
    driver.quit()