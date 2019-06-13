from selenium.webdriver.common.by import By
from under_the_hood.multyusable import GBtool
from selenium.common.exceptions import WebDriverException

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

    FILTER_BLOCK = (By.CSS_SELECTOR, '.before-content-title')  # Панель фильтрации
    COUNTER = (By.CSS_SELECTOR, '.content__title-left')  # Счетчик записей
    ONLINE_NOW = (By.CSS_SELECTOR, '.online-checkbox .form-checkbox')  # Чек-бокс онлайн
    INVITED_MENU = (By.CSS_SELECTOR, '.invited-menu')  # Меню приглашенных бустеров
    BOOSTERS_BODY = (By.CSS_SELECTOR, '.boosters__body')  # Список топ-бустеров
    PAGINATOR = (By.CSS_SELECTOR, '.paginator')  # Список страниц
    BOOSTER = (By.CSS_SELECTOR, '.booster')  # Строка бустера
    GAME_CHOOSER = (By.CSS_SELECTOR, '.chooser__title')  # блок выпадающего списка
    CHOOSER_ITEM = (By.CSS_SELECTOR, '.chooser__item')
    DROP_DOWN = (By.CSS_SELECTOR, '.chooser__dropdown')  # ВЫпадающий список
    GM_CH = (By.CSS_SELECTOR, '.chooser')
    INVITE_BTN = (By.CSS_SELECTOR, '.btn--primary')  # Кнопка найм
    INVITED_BOOSTER = (By.CSS_SELECTOR, '.booster-row')  # приглашенный бустер
    DEZINVITE = (By.CSS_SELECTOR, '.booster-row__close')  # Удалить бустера
    # CHOOSER_ITEM_NEW = (By.CSS_SELECTOR, '')





class TopBoostPage(BasePage):
    """Домашняя страница, после клика на лого"""



    def check_components(self):
        """Проверка компонентов топ бустеров"""

        gb_tool = GBtool(self.driver)

        filter_block = Locators.FILTER_BLOCK
        gb_tool.check_exists_by_css(css=filter_block[1], name='Панель фильтрации')

        counter = Locators.COUNTER
        gb_tool.check_exists_by_css(css=counter[1], name='Счетчик')

        checkbox = Locators.ONLINE_NOW
        gb_tool.check_exists_by_css(css=checkbox[1], name='Чек бокс пользователей онлайн')

        inv_menu = Locators.INVITED_MENU
        gb_tool.check_exists_by_css(css=inv_menu[1], name='Менб приглашенных бустеров')

        boost_list = Locators.BOOSTERS_BODY
        gb_tool.check_exists_by_css(css=boost_list[1], name='Список топ-бустеров')

        paging = Locators.PAGINATOR
        gb_tool.check_exists_by_css(css=paging[1], name='Список страниц')

    def check_sort_by_service(self):
        """Сортировка по услуге"""


        gb_tool = GBtool(self.driver)
        service = self.driver.find_elements_by_css_selector(Locators.GM_CH[1])[2]
        name = 'Панель выбора суслуги'

        gb_tool.select_a_game('All games')
        z = gb_tool.is_active(service, name)
        assert_equal(z, 0, 'Сценарий неверен')
        gb_tool.select_a_game('World of Warcraft')
        z = gb_tool.is_active(service, name)
        assert_equal(z, 1, 'Сценарий неверен')

        game_list = ['World of Warcraft', 'Counter-Strike', 'Overwatch', 'Dota 2', 'League of Legends']
        i = 0
        while i < len(game_list):

            self.service_check(game_list[i])
            print('Услуги ' + game_list[i] + ' сошлись')
            i += 1

    def service_check(self, name):
        """Проверка строк"""

        gb_tool = GBtool(self.driver)
        service = self.driver.find_elements_by_css_selector(Locators.GAME_CHOOSER[1])[2]
        dpdwn = self.driver.find_elements_by_css_selector(Locators.DROP_DOWN[1])[2]

        service_dict = {

            'World of Warcraft': ['All services', 'Powerleveling', 'PVP', 'Dungeons', 'Raids', 'Mounts', 'Glories', 'Coaching',
                                  'Other services'],
            'Counter-Strike': ['All services', 'Calibration', 'Rank boost', 'Coaching', 'Other services'],
            'Overwatch': ['All services', 'Skill rating boost', 'Win boost', 'Placement matches', 'LVL boost', 'Coaching', 'Other services'],
            'Dota 2': ['All services', 'Boost solo mmr', 'Calibration', 'Boost party mmr', 'Low priority', 'Coaching',
                       'Other services'],
            'League of Legends': ['All services', 'Division boost', 'Win boost', 'Calibration', 'Coaching', 'Other services']

        }

        gb_tool.select_a_game(name)
        i = 0
        service.click()

        while i < len(service_dict[name]):

            row = dpdwn.find_elements_by_css_selector(Locators.CHOOSER_ITEM[1])[i]
            assert_equal(row.text, service_dict[name][i])
            i += 1
        service.click()

    def search_check(self, name):

        gb_tool = GBtool(self.driver)
        gb_tool.search(name)

        booster = self.driver.find_elements_by_css_selector(Locators.BOOSTER[1])[0]
        booster_name = booster.find_element_by_css_selector('.booster__playername')

        assert_equal(booster_name.text, name, 'Поиск верен')

    def invite_booster(self):

        gb_tool = GBtool(self.driver)
        time.sleep(1)
        hire_btn = self.driver.find_element_by_css_selector(Locators.INVITE_BTN[1])
        booster = self.driver.find_elements_by_css_selector(Locators.BOOSTER[1])[0]
        booster_name = booster.find_element_by_css_selector('.booster__playername')
        booster_name = booster_name.text
        hire_btn.click()

        invited_booster = self.driver.find_element_by_css_selector(Locators.INVITED_BOOSTER[1])
        invited_booster_name = invited_booster.find_element_by_css_selector('.invited-menu--dark')
        invited_booster_name = invited_booster_name.text


        hire_btn.click()
        gb_tool.check_exists_by_css('.booster-row', 'Приглашенный бустер', reverse=True)
        # assert_equal(x, 1, 'Окно не заполнено бустером')
        assert_equal(booster_name, invited_booster_name, 'Имена не сходятся')

    def dezinvite_boost(self):

        gb_tool = GBtool(self.driver)
        delete = self.driver.find_element_by_css_selector(Locators.DEZINVITE[1])
        time.sleep(1)
        delete.click()
        gb_tool.check_exists_by_css('.booster-row', 'Приглашенный бустер')
        # time.sleep(1)
        # assert_equal(x, 0, 'Окно заполнено бустером')






















