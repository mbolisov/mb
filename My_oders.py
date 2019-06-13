from selenium.webdriver.common.by import By
from under_the_hood.multyusable import GBtool
from under_the_hood.Constructor import Constructor
import time
from nose.tools import assert_equal, assert_true
from selenium import webdriver
import re


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver



class Locators(object):
    """ Локаторы страницы мои заказы"""

    NOORDERS_BLOCK = (By.CSS_SELECTOR, '.order--none')  # Блок создания первого заказа
    ORDERS_CAT = (By.CSS_SELECTOR, '.rounded-block')  # Заказы по категориям
    ORDERS_COUNT = (By.CSS_SELECTOR, '.content__title-left')  # Счетчик заказов
    ORDERS = (By.CSS_SELECTOR, '.content__body')  # Список заказов
    NEW_ORDER_BTN_LEFT = (By.CSS_SELECTOR, '.hz-btn--second')  # Кнопка нового заказа на плашке "Новый заказ"
    NEW_ORDER_BTN_RIGHT = (By.CSS_SELECTOR, '.page-body__right .hz-btn')  # Кнопка нового заказа на блоке спарва
    GAME_CHOOSER = (By.CSS_SELECTOR, '.chooser__title')  # Выпадаюищй список с играми
    DROP_DOWN = (By.CSS_SELECTOR, '.chooser__dropdown')  # Выпадающий список игр
    CURRENT_GAME = (By.CSS_SELECTOR, '.chooser__item--title')
    CAT_COUNT = (By.CSS_SELECTOR, '.oval-btn')  # Кол-во игр в категории
    ORDER = (By.CSS_SELECTOR, '.or')








class MyOdersPage(BasePage):
    """Домашняя страница, после клика на лого"""



    def check_components_no_orders(self):
        """Проверка компонентов нового байера"""

        gb_tool = GBtool(self.driver)

        no_orders_block = Locators.NOORDERS_BLOCK
        gb_tool.check_exists_by_css(css=no_orders_block[1], name='Плашка первого заказа')

        orders_cat = Locators.ORDERS_CAT
        gb_tool.check_exists_by_css(css=orders_cat[1], name='Блок категорий заказа')

        orders_count = Locators.ORDERS_COUNT
        gb_tool.check_exists_by_css(css=orders_count[1], name='Счетчик заказов')

    def check_components_with_orders(self):
        """Проверка компонентов баера с заказами"""

        gb_tool = GBtool(self.driver)

        orders = Locators.ORDERS
        gb_tool.check_exists_by_css(orders)

        orders_cat = Locators.ORDERS_CAT
        gb_tool.check_exists_by_css(orders_cat)

        orders_count = Locators.ORDERS_COUNT
        gb_tool.check_exists_by_css(orders_count)

    def new_order(self, btn ='left'):
        """Создание заказа"""

        constructor = Constructor(self.driver)

        if btn == 'left':

            Btn = Locators.NEW_ORDER_BTN_LEFT
            botton = self.driver.find_element_by_css_selector(Btn)
            botton.click()
            constructor.is_constructor_download()

        if btn == 'right':

            Btn = Locators.NEW_ORDER_BTN_RIGHT
            boton = self.driver.find_element_by_css_selector(Btn)
            boton.click()
            constructor.is_constructor_download()

    def do_sort_by_game(self, name):
        """Проверка сортировки по игре"""

        games_dict = {
            'all': 0,
            'World of Warcraft': 1,
            'Counter-Strike': 2,
            'Overwatch': 3,
            'Dota 2': 4,
            'League of legends': 5

        }

        gb_tool = GBtool(self.driver)

        chooser = Locators.GAME_CHOOSER
        chooser = self.driver.find_element_by_css_selector(chooser)
        chooser.click()

        cur_game = Locators.CURRENT_GAME
        cur_game = self.driver.find_elements_by_css_selector(cur_game[1])[games_dict[name]]
        cur_game.click()

        game_name = chooser.text
        assert_equal(game_name, name, 'Название выбранной игры неверно')

        i = 1






    def do_sort_by_cat(self, name):
        """Проверка сортировки по категориям"""

        cat_dict = {
            'All orders': 1,
            'Auction': 2,
            'In progress': 3,
            "Waiting": 4,
            'Done': 5,
            'Drafts': 6
            }

        cat_count = Locators.CAT_COUNT
        time.sleep(2)
        cat_count = self.driver.find_elements_by_css_selector(cat_count[1])[cat_dict[name]]
        cat_count.click()
        count_cat = cat_count.text
        assert_equal(self.string_count(), count_cat, 'Значения не равны')


    def string_count(self):
        """Возвращает значение строк в таблице после сортировки"""

        count = Locators.ORDERS_COUNT
        count = self.driver.find_element_by_css_selector(count[1])
        count = count.text
        count = re.sub(r"\D", '', count)
        return count

















