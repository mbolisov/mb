from selenium.webdriver.common.by import By
from under_the_hood.multyusable import GBtool
from selenium.common.exceptions import WebDriverException

from under_the_hood.Constructor import Constructor
import time
from nose.tools import assert_equal, assert_true
from selenium import webdriver
import re


class Locators(object):

    DEPOSIT_FUNDS = (By.CSS_SELECTOR, '.deposit-form')  # Блок внести средства
    HISTORY = (By.CSS_SELECTOR, '.history')  # Блок история
    BALANCE = (By.CSS_SELECTOR, '.balance')  # Блок баланс

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class Balance(BasePage):
    """ Баланс """

    def check_components(self):
        """Проверка компонентов топ бустеров"""

        gb_tool = GBtool(self.driver)

        time.sleep(1)
        deposit_funds = self.driver.find_element(*Locators.DEPOSIT_FUNDS)
        gb_tool.check_exists_by_css(css=deposit_funds, name='Блок внести средства')

        history = self.driver.find_element(*Locators.HISTORY)
        gb_tool.check_exists_by_css(css=history, name='Блок история')

        balance = self.driver.find_element(*Locators.BALANCE)
        gb_tool.check_exists_by_css(css=balance, name='Блок баланс')
