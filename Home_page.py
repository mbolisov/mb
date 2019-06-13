# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import time
from under_the_hood.multyusable import GBtool


class Locators(object):
    """ Локаторы домашней страницы"""

    HEADER_LOGO = (By.CSS_SELECTOR, '.header__logo svg')  # логосайта
    WELCOME = (By.CSS_SELECTOR, '.welcome')  # Блок создания первого заказа
    TOP_BOOSTRS = (By.CSS_SELECTOR, '.dashboard-page__boosters-list')  # Список топ бустеров
    BALANCE = (By.CSS_SELECTOR, '.balance')  # Блок баланс
    FAQ = (By.CSS_SELECTOR, '.faq-slider')  # Блок справка
    NOTIFICATIONS_LIST = (By.CSS_SELECTOR, '.notifications')  # Блок уведомлений
    ORDERS = (By.CSS_SELECTOR, '.orders-list')  # Новые заказы





class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    """Домашняя страница, после клика на лого"""

    def goto(self):
        """Переход на домашнюю страницу"""

        logo = self.driver.find_element(*Locators.HEADER_LOGO)
        logo.click()

    def check_components_no_orders(self):
        """Проверка компонентов нового байера"""

        welcome = Locators.WELCOME
        GBtool.check_exists_by_css(self, css=welcome[1], name='Блок создания заказа')
        top_bst = Locators.TOP_BOOSTRS
        GBtool.check_exists_by_css(self, css=top_bst[1], name='Блок топ бустеров')
        balance = Locators.BALANCE
        GBtool.check_exists_by_css(self, css=balance[1], name='Блок баланс')
        faq = Locators.FAQ
        GBtool.check_exists_by_css(self, css=faq[1], name='F.A.Q.')

    def check_components_with_order(self):
        """Проверка компонентнов байера делавшего заказы"""

        time.sleep(3)
        notification = self.driver.find_element(*Locators.NOTIFICATIONS_LIST)
        GBtool.check_exists_by_css(self, css=notification, name='Блок уведомлений')
        balance = self.driver.find_element(*Locators.BALANCE)
        GBtool.check_exists_by_css(self, css=balance, name='Блок баланс')
        faq = self.driver.find_element(*Locators.FAQ)
        GBtool.check_exists_by_css(self, css=faq, name='F.A.Q.')

    def check_components_bosoter_no_oders(self):
        """Проверка компонентнов нового бустера"""

        welcome = self.driver.find_element(*Locators.WELCOME)
        GBtool.check_exists_by_css(self, css=welcome, name='Начать знакомство ')
        oders = self.driver.find_element(*Locators.ORDERS)
        GBtool.check_exists_by_css(self, css=oders, name='Блок топ бустеров')
        balance = self.driver.find_element(*Locators.BALANCE)
        GBtool.check_exists_by_css(self, css=balance, name='Блок баланс')
        faq = self.driver.find_element(*Locators.FAQ)
        GBtool.check_exists_by_css(self, css=faq, name='F.A.Q.')



















