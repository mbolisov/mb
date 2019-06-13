# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
import selenium
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time
from under_the_hood import log_in_page
import logging
from selenium.webdriver.common.action_chains import ActionChains
from xml import etree
from nose.tools import assert_equal, assert_true


class Locators(object):
    """Локаторы"""

    HEADER_LOGO = (By.CSS_SELECTOR, '.header__logo svg')
    MENU_BTNS = (By.CSS_SELECTOR, '.menu__item')
    PROFILE = (By.CSS_SELECTOR, '.header__ava-link')
    DROPDOWN_MENU_STRINGS = (By.CSS_SELECTOR, '.drop-down__link')
    CONSTRUCTOR = (By.CSS_SELECTOR, '.header__new-order-btn--lg')
    GAME_CHOOSER = (By.CSS_SELECTOR, '.chooser__title')  # Выпадаюищй список с играми
    BODY = (By.CSS_SELECTOR, '.content__body')  # Результирующая таблица для сортировки
    GAME_ICON = (By.CSS_SELECTOR, '.order__game-icon')  # Иконка игры
    CURRENT_GAME = (By.CSS_SELECTOR, '.chooser__item')  # Строка игры
    INPUT = (By.CSS_SELECTOR, '.div-input')  # Поле поиска
    SRCH_BTN = (By.CSS_SELECTOR, '.div-input__icon')  # Кнопка поиск
    DRPDWN = (By.CSS_SELECTOR, '.drop-down__menu')  # Выпадающий список меню
    SERVICE = (By.CSS_SELECTOR, '.choose-service')
    DROP_DOWN = (By.CSS_SELECTOR, '.chooser__dropdown')
    GAME = (By.CSS_SELECTOR, '.choose-game')
    CHOOSER_ITEM = (By.CSS_SELECTOR, '.chooser__item')
    LANGUAGE_CHOSER = (By.CSS_SELECTOR, '.choose-language')
    LANGUAGE = (By.CSS_SELECTOR, '.chooser__item')
    LANGUAGE_HIDE = (By.CSS_SELECTOR, '.chooser__corner')

    ORDER = (By.CSS_SELECTOR, '.orders-item ')
    BOOSTER = (By.CSS_SELECTOR, 'booster')
    ORDERS = (By.CSS_SELECTOR, '.order')

class Game_icons(object):
    """Локаторы иконок игр"""

    FIND_ORDERS_WOW = (By.CSS_SELECTOR, '.header__icon')
    TOP_BOOSTERS_WOW = (By.CSS_SELECTOR, '.game-icons__icon')
    MY_ORDERS_WOW = (By.CSS_SELECTOR, '.order__game-icon')




class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class GBtool(BasePage):




    def check_exists_by_css(self, css, name, reverse=False):
        """Проверка наличия эл-тов на странице"""

        # element = self.driver.find_element_by_css_selector(css)
        # element.is_dysplayed
        # element = self.driver
        # z = '.' + css.get_attribute('class')
        # z = z.split(' ')[locator]


        try:
            time.sleep(1)
            self.driver.find_element_by_css_selector(css)
            logging.info("Элемент" + name + " загрузился.")
            print('Элемент ' + name + ' загрузился.')
            x = 1
        except NoSuchElementException:
            logging.info('Элемент ' + name + ' не загрузился.')
            print('Элемент ' + name + ' не загрузился.')
            x = 0
        if reverse == True:
            z = 0
            end = 'а нет'
        else :
            z = 1
            end = ' есть'

        assert_equal(x, z, 'Элемент' + end)

    def goto_tab(self, home = False, my_orders=False, popular=False, top_boost=False, constructor=False):
        """Переход на вкладку"""
        tab_dict = {
            'my_orders': Locators.MENU_BTNS[1],
            'popular': Locators.MENU_BTNS[1],
            'top_boost': Locators.MENU_BTNS[1]


        }

        if home != 0:
            tab = self.driver.find_element_by_css_selector(Locators.HEADER_LOGO[1])
            tab.click()
            logging.info('Переход на домашнюю страницу...')

        if my_orders != 0:
            time.sleep(5)
            tab = self.driver.find_elements_by_css_selector(tab_dict['my_orders'])[0]
            time.sleep(5)
            tab.click()
            logging.info("Переход на вкладку 'Мои заказы'... ")

        if popular != 0:

            time.sleep(5)
            tab = self.driver.find_elements_by_css_selector(tab_dict['popular'])[1]
            time.sleep(5)
            tab.click()
            logging.info("Переход на вкладку 'Популярные услуги'... ")

        if top_boost != 0:

            time.sleep(5)
            tab = self.driver.find_elements_by_css_selector(tab_dict['top_boost'])[2]
            time.sleep(5)
            tab.click()
            logging.info("Переход на вкладку 'Топ бустеры'... ")

        if constructor != 0:
            tab = self.driver.find_element_by_css_selector(Locators.CONSTRUCTOR[1])
            tab.click()
            logging.info("Открытие конструктора... ")


    def go_to_tab_booster(self, home = False, search_orders = False, my_orders = False, auto = False, top_boost = False):

        if search_orders != 0:
            tab = self.driver.find_elements(*Locators.MENU_BTNS)[0]
            time.sleep(1)
            tab.click()

        if my_orders != 0:
            tab = self.driver.find_elements(*Locators.MENU_BTNS)[1]
            time.sleep(1)
            tab.click()

        if auto != 0:
            tab = self.driver.find_elements(*Locators.MENU_BTNS)[2]
            time.sleep(1)
            tab.click()

        if top_boost != 0:
            tab = self.driver.find_elements(*Locators.MENU_BTNS)[3]
            time.sleep(1)
            tab.click()

        if home != 0:
            tab = self.driver.find_elements(*Locators.HEADER_LOGO)
            time.sleep(1)
            tab.click()



    def go_to_menu(self, name):
        """Переход по категориям профиля пользователя"""

        menu_dict = {
            'BALANCE': 0,
            'DASHBOARD': 1,
            'SETTINGS': 2,
            'FAQ': 3,
            'LOG OUT': 4
        }

        profile = self.driver.find_element_by_css_selector(Locators.PROFILE[1])
        self.mouseover(profile)
        drpd_dwn = self.driver.find_element(*Locators.DRPDWN)
        self.check_exists_by_css(drpd_dwn, name='ВЫпадающий список')
        row = self.driver.find_elements(*Locators.DROPDOWN_MENU_STRINGS)[menu_dict[name]]
        row.click()








    def mouseover(self, element):

        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()



    def relog(self, log, pswrd):

        time.sleep(3)
        profile_icon = self.driver.find_element(*Locators.PROFILE)
        GBtool.mouseover(self, profile_icon)
        log_out = self.driver.find_elements_by_css_selector('.drop-down__item')[4]
        log_out.click()
        log_in_page.MainPage.login(self, mail=log, password=pswrd)

    def highlight(self, element):
        """Highlights (blinks) a Selenium Webdriver element"""
        driver = element._parent

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 2px solid red;")
        time.sleep(.3)
        apply_style(original_style)

    def select_a_game(self, name):
        """Выставление сортировки"""

        games_dict = {
            'All games': [0, 3],
            'World of Warcraft': [1, 4],
            'Counter-Strike': [2, 5],
            'Overwatch': [3, 6],
            'Dota 2': [4, 7],
            'League of Legends': [5, 8]

        }

        gb_tool = GBtool(self.driver)

        chooser = Locators.GAME_CHOOSER
        x = self.driver.current_url

        if x == 'https://dev.gamersbay.com/boosters':

            chooser = self.driver.find_elements_by_css_selector(chooser[1])[1]
            chooser.click()
            cur_game = Locators.CURRENT_GAME
            time.sleep(1)
            cur_game = self.driver.find_elements_by_css_selector(cur_game[1])[games_dict[name][1]]
            time.sleep(2)
            cur_game.click()
            game_name = chooser.text
            assert_equal(game_name, name, 'Название выбранной игры неверно')

        if x == 'https://dev.gamersbay.com/user#/orders':
            chooser = self.driver.find_element_by_css_selector(chooser[1])
            chooser.click()
            cur_game = Locators.CURRENT_GAME
            cur_game = self.driver.find_elements_by_css_selector(cur_game[1])[games_dict[name][0]]
            cur_game.click()
            game_name = chooser.text
            assert_equal(game_name, name, 'Название выбранной игры неверно')

        if x == 'https://dev.gamersbay.com/user#/find_orders':
            time.sleep(1)
            chooser = self.driver.find_element(*Locators.GAME)
            chooser.click()
            cur_game = self.driver.find_elements(*Locators.CURRENT_GAME)[games_dict[name][1]]
            time.sleep(1)
            cur_game.click()
        if name != 'All games':
                chooser.click()

    def select_a_service(self):

            service = self.driver.find_element(*Locators.SERVICE)
            time.sleep(1)
            service.click()
            pwrlvl = service.find_elements(*Locators.CHOOSER_ITEM)[1]
            pwrlvl.click()
            service.click()





    def do_sort_by_game(self, name):
        """Проверка сортировки по игре"""

        # games_dict = {
        #     'all': 0,
        #     'World of Warcraft': [1, 4],
        #     'Counter-Strike': [2, 5],
        #     'Overwatch': [3, 6],
        #     'Dota 2': [4, 7],
        #     'League of legends': [5, 8]
        #
        # }
        #
        #
        # gb_tool = GBtool(self.driver)
        #
        # chooser = Locators.GAME_CHOOSER
        # x = self.driver.current_url
        #
        # if x == 'https://dev.gamersbay.com/boosters':
        #
        #     chooser = self.driver.find_elements_by_css_selector(chooser[1])[1]
        #     chooser.click()
        #     cur_game = Locators.CURRENT_GAME
        #     time.sleep(1)
        #     cur_game = self.driver.find_elements_by_css_selector(cur_game[1])[games_dict[name][1]]
        #     time.sleep(1)
        #     cur_game.click()
        # else:
        #     chooser = self.driver.find_element_by_css_selector(chooser[1])
        #     chooser.click()
        #     cur_game = Locators.CURRENT_GAME
        #     cur_game = self.driver.find_elements_by_css_selector(cur_game[1])[games_dict[name][0]]
        #     cur_game.click()
        #
        # game_name = chooser.text
        # assert_equal(game_name, name, 'Название выбранной игры неверно')

        self.select_a_game(name)
        x = self.driver.current_url
        if x == 'https://dev.gamersbay.com/boosters':
            locator = Locators.BOOSTER
            img = Game_icons.TOP_BOOSTERS_WOW

        if x == 'https://dev.gamersbay.com/user#/orders':
            locator = Locators.ORDERS
            img = Game_icons.MY_ORDERS_WOW

        if x == 'https://dev.gamersbay.com/user#/find_orders':
            locator = Locators.ORDER
            img = Game_icons.FIND_ORDERS_WOW

        i = 0
        if name == 'World of Warcraft':
            src_etalon = 'https://dev.gamersbay.com/images/games/1/icons/icon.svg'
            time.sleep(1)
            while i < 20:
                time.sleep(1)
                row = self.driver.find_elements_by_css_selector(locator[1])[i]
                game = row.find_elements_by_css_selector(img[1])[0]
                src = game.get_attribute('src')
                time.sleep(1)
                assert_equal(src, src_etalon, 'Игра не соотвествует фильтру')
                print('Строка %d из 20 соответсвует сортировке по ' % (i+1) + name)
                i += 1
        self.select_a_game(name)


    def is_active(self, element, name):
        """ПРоверяем активен ли элемент"""


        try:
            element.click()
            x = 'Активен'

        except WebDriverException:
            x = 'Неактивен'


        if x == 'Активен':
            element.click()
            print('Элемент ' + name + ' доступен')
            z = 1


        else:
            print('Элемент ' + name + ' не актвиен')
            z = 0

        return z



    def search(self, str):
        """Функция поиска"""

        srch_field = self.driver.find_element_by_css_selector(Locators.INPUT[1])
        srch_input = srch_field.find_element_by_css_selector('.div-input__input')
        btn = self.driver.find_element_by_css_selector(Locators.SRCH_BTN[1])

        srch_field.click()
        srch_input.send_keys(str)
        btn.click()



    def check_sort_by_service(self):
        """Сортировка по услуге"""

        service = self.driver.find_element(*Locators.SERVICE)
        name = 'Панель выбора суслуги'

        self.select_a_game('World of Warcraft')
        z = self.is_active(service, name)
        assert_equal(z, 1, 'Сценарий неверен')

        self.select_a_game('All games')
        z = self.is_active(service, name)
        assert_equal(z, 0, 'Сценарий неверен')

        game_list = ['World of Warcraft', 'Counter-Strike', 'Overwatch', 'Dota 2', 'League of Legends']
        i = 0
        while i < len(game_list):

            self.select_a_game(game_list[i])
            self.service_check(game_list[i])
            print('Услуги ' + game_list[i] + ' сошлись')
            i += 1

    def check_sort_service_boost(self):
        """Сортировака по услуге бустера"""


        etalon = 'Select a service\nAll services\nPowerleveling\nPVP\nDungeons\nRaids\nMounts\nGlories\nCoaching\nOther services\nAll services\nCalibration\nRank boost\nCoaching\nOther services\nAll services\nSkill rating boost\nWin boost\nPlacement matches\nLVL boost\nCoaching\nOther services\nAll services\nBoost solo mmr\nCalibration\nBoost party mmr\nLow priority\nCoaching\nOther services\nAll services\nDivision boost\nWin boost\nCalibration\nCoaching\nOther services'
        game_list = ['World of Warcraft', 'Counter-Strike', 'Overwatch', 'Dota 2', 'League of Legends']
        i = 0
        while i < len(game_list):
            self.select_a_game(game_list[i])
            i += 1

        service = self.driver.find_element(*Locators.SERVICE)
        service.click()
        assert_equal(etalon, service.text, 'какой то сервис не тот')

        i = 0
        while i < len(game_list):
            self.select_a_game(game_list[i])
            i += 1





    def service_check(self, name):
        """Проверка строк"""

        service = self.driver.find_element(*Locators.SERVICE)
        dpdwn = service.find_element(*Locators.DROP_DOWN)


        service_dict = {

            'World of Warcraft': ['All services', 'Powerleveling', 'PVP', 'Dungeons', 'Raids', 'Mounts', 'Glories', 'Coaching',
                                  'Other services'],
            'Counter-Strike': ['All services', 'Calibration', 'Rank boost', 'Coaching', 'Other services'],
            'Overwatch': ['All services', 'Skill rating boost', 'Win boost', 'Placement matches', 'LVL boost', 'Coaching', 'Other services'],
            'Dota 2': ['All services', 'Boost solo mmr', 'Calibration', 'Boost party mmr', 'Low priority', 'Coaching',
                       'Other services'],
            'League of Legends': ['All services', 'Division boost', 'Win boost', 'Calibration', 'Coaching', 'Other services']

        }

        # self.select_a_game(name)
        i = 0
        service.click()

        while i < len(service_dict[name]):

            row = dpdwn.find_elements(*Locators.CHOOSER_ITEM)[i]
            assert_equal(row.text, service_dict[name][i], 'Разбой услуг')
            i += 1
        service.click()


    def language_set(self, rus = False, eng = False):
        """Выбор языка"""


        time.sleep(1)
        language_choose = self.driver.find_element(*Locators.LANGUAGE_CHOSER)
        lang_hide = self.driver.find_element(*Locators.LANGUAGE_HIDE)
        lang_hide.click()

        lang = language_choose.find_elements(*Locators.LANGUAGE)[1]
        lang.click()
        lang = language_choose.find_elements(*Locators.LANGUAGE)[2]
        lang.click()

        if rus == True :
            i = 2
        if eng == True:
            i = 1



        lang = language_choose.find_elements(*Locators.LANGUAGE)[i]
        lang.click()
        lang_hide.click()














