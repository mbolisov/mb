from selenium.webdriver.common.by import By
from under_the_hood.multyusable import GBtool
import time
import re
from nose.tools import assert_equal, assert_true


class Locators(object):


    FILTER = (By.CSS_SELECTOR, '.filters__controls')
    MENU = (By.CSS_SELECTOR, '.menu')
    LIST = (By.CSS_SELECTOR, '.orders-list')
    TITLE = (By.CSS_SELECTOR, '.filters__title')
    GAME_ICON = (By.CSS_SELECTOR, '.game-icon')
    ORDER = (By.CSS_SELECTOR, '.orders-item')




class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MyOrders(BasePage):
    """ Баланс """

    def check_components(self):
        """Проверка компонентов топ бустеров"""

        gb_tool = GBtool(self.driver)

        time.sleep(1)
        filter = Locators.FILTER
        gb_tool.check_exists_by_css(css=filter[1], name='выбор игры')

        menu = Locators.MENU
        gb_tool.check_exists_by_css(css=menu[1], name='Меню')

        orders_list = Locators.LIST
        gb_tool.check_exists_by_css(css=orders_list[1], name='Список заказов')


    def check_game(self):
        """Проверка сортировки по игре"""

        gb_tool = GBtool(self.driver)

        time.sleep(1)
        gm = 'World of Warcraft'
        gb_tool.select_a_game(gm)
        time.sleep(2)
        ttl = self.driver.find_element(*Locators.TITLE)
        ttl = ttl.text
        count = int(re.findall(r'\d+', ttl)[0])
        etalon = 'https://dev.gamersbay.com/images/games/1/icons/icon.svg'

        i = 0
        while i<count:
            time.sleep(2)
            order = self.driver.find_elements(*Locators.ORDER)[i]
            game_icon = order.find_element(*Locators.GAME_ICON)
            icon = game_icon.get_attribute('src')
            assert_equal(etalon, icon, 'не сошлось')
            print('Строка %d из %d соответсвует сортировке по ' % ((i+1), count) + gm)
            i+=1











