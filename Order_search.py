from selenium.webdriver.common.by import By
from under_the_hood.multyusable import GBtool
import time
from nose.tools import assert_equal, assert_true


class Locators(object):

    LANGUAGE_CHOOSER = (By.CSS_SELECTOR, '.choose-language')
    GAME_CHOOSER = (By.CSS_SELECTOR, '.choose-game')
    SERVICE_CHOOSER = (By.CSS_SELECTOR, '.choose-service')
    FAV = (By.CSS_SELECTOR, '.scrollbar')
    FILTER = (By.CSS_SELECTOR, '.filter')
    ORDERS = (By.CSS_SELECTOR, '.orders-list')
    NAME = (By.CSS_SELECTOR, '.title')
    ORDRITM = (By.CSS_SELECTOR, '.orders-item')
    LANG_ICON = (By.CSS_SELECTOR, '[alt="RU"]')
    ORDER = (By.CSS_SELECTOR, '.orders-item')
    LANG_CLOSE = (By.CSS_SELECTOR, '.chooser__corner')
    SHOW_MORE = (By.CSS_SELECTOR, '.btn--show-more')
    PLACE_BID = (By.CSS_SELECTOR, '.btn--primary')
    STAVOCHKA = (By.CSS_SELECTOR, '.bid')
    ORDER_BTNS = (By.CSS_SELECTOR, '.sidebar__btn')
    DIALOG = (By.CSS_SELECTOR, '.dialog-window')




class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class OrderSearch(BasePage):
    """ Баланс """

    def check_components(self):
        """Проверка компонентов топ бустеров"""

        gb_tool = GBtool(self.driver)

        time.sleep(1)
        # lc = self.driver.find_element(*Locators.LANGUAGE_CHOOSER)
        language = Locators.LANGUAGE_CHOOSER
        gb_tool.check_exists_by_css(css=language[1], name='выбор языка')

        game = Locators.GAME_CHOOSER
        gb_tool.check_exists_by_css(css=game[1], name='Выбор игры')

        service = Locators.SERVICE_CHOOSER
        gb_tool.check_exists_by_css(css=service[1], name='Услуга')

        fav = Locators.FAV
        gb_tool.check_exists_by_css(css=fav[1], name='Избранное')

        filter = Locators.FILTER
        gb_tool.check_exists_by_css(css=filter[1], name='Фильтр')

        orders = Locators.ORDERS
        gb_tool.check_exists_by_css(css=orders[1], name='Заказы')


    # def check_sort_by_service(self):
    #     """Сортировка по услуге"""
    #
    #
    #     gb_tool = GBtool(self.driver)
    #     service = self.driver.find_elements_by_css_selector(Locators.GM_CH[1])[2]
    #     name = 'Панель выбора суслуги'
    #
    #     gb_tool.select_a_game('All games')
    #     z = gb_tool.is_active(service, name)
    #     assert_equal(z, 0, 'Сценарий неверен')
    #     gb_tool.select_a_game('World of Warcraft')
    #     z = gb_tool.is_active(service, name)
    #     assert_equal(z, 1, 'Сценарий неверен')
    #
    #     game_list = ['World of Warcraft', 'Counter-Strike', 'Overwatch', 'Dota 2', 'League of Legends']
    #     i = 0
    #     while i < len(game_list):
    #
    #         self.service_check(game_list[i])
    #         print('Услуги ' + game_list[i] + ' сошлись')ё
    #         i += 1


    def check_sort_by_service(self):
        """Проверяет сортировку по услуге"""


        gb_tool = GBtool(self.driver)
        gb_tool.select_a_game('World of Warcraft')
        gb_tool.select_a_service()


        i = 0
        while i < 20:
            ordritm = self.driver.find_elements(*Locators.ORDRITM)[i]
            name = ordritm.find_element(*Locators.NAME)
            name = name.text
            name = name[18:31]
            assert_equal(name, 'Powerleveling', 'не сошлось')
            print('Запись %d из 20 отсортирвоана по улсуге ' % (i+1) + name)
            i += 1

        gb_tool.select_a_service()

    #
    # def check_language_sort(self):
    #     """Проверяет сортировку по языку"""
    #
    #     gb_tool = GBtool(self.driver)
    #     gb_tool.language_set(eng=True)

    def lang_checker(self, rus = False, eng = False):
        """Проверка сортировки по игре"""

        gb_tool = GBtool(self.driver)
        gb_tool.language_set(eng=True)

        i = 0
        if eng == True:
            lang_name = 'английскому языку'
            src_etalon = 'https://dev.gamersbay.com/images/interface/icon/lang/flag--en.svg'
            time.sleep(1)
            while i < 20:
                time.sleep(2)
                row = self.driver.find_elements(*Locators.ORDER)[i]
                lang = row.find_element_by_css_selector('[alt="EN"]')
                src = lang.get_attribute('src')
                time.sleep(1)
                assert_equal(src, src_etalon, 'Язык не соотвествует фильтру')
                print('Заказ %d из 20 соответсвует сортировке по ' % (i+1) + lang_name)
                i += 1

    def delete(self):

        gb_tools = GBtool(self.driver)
        order = self.driver.find_elements(*Locators.ORDER)[0]
        delete = order.find_elements(*Locators.ORDER_BTNS)[1]
        delete.click()
        dialog = Locators.DIALOG
        gb_tools.check_exists_by_css(css=dialog[1], name='Окно удаления')

    def fav(self):

        gb_tool = GBtool(self.driver)
        order = self.driver.find_elements(*Locators.ORDER)[0]
        fav = order.find_elements(*Locators.ORDER_BTNS)[0]
        fav.click()










