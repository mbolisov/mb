from selenium.webdriver.common.by import By
from under_the_hood.multyusable import GBtool
from selenium.common.exceptions import WebDriverException

from under_the_hood.Constructor import Constructor
import time
from nose.tools import assert_equal, assert_true
from selenium import webdriver
import re


class Locators(object):

    PASSWORD = (By.CSS_SELECTOR, '.password')  # Пароль
    FAQ = (By.CSS_SELECTOR, '.faq-slider')  # FAQ
    USERPIC = (By.CSS_SELECTOR, '.userpic')  # Аватар
    CARD = (By.CSS_SELECTOR, '.card')  # Карточка информации



class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class Settings(BasePage):
    """ Настроечки """

    def check_components(self):
        """Проверка компонентов топ бустеров"""

        gb_tool = GBtool(self.driver)

        time.sleep(1)
        password = self.driver.find_element(*Locators.PASSWORD)
        gb_tool.check_exists_by_css(css=password, name='Блок смены пароля')

        faq = self.driver.find_element(*Locators.FAQ)
        gb_tool.check_exists_by_css(css=faq, name='Блок справки ')

        usrpic = self.driver.find_element(*Locators.USERPIC)
        gb_tool.check_exists_by_css(css=usrpic, name='Аватар')

        card = self.driver.find_element(*Locators.CARD)
        gb_tool.check_exists_by_css(css=card, name="Карточка пользователя")

