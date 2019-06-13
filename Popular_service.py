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
    """Локаторы страницы популярные заказы"""

# ###########***************************Вкладка на хуй не работает**********************
 