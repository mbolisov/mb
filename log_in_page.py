# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import time
from under_the_hood.multyusable import GBtool
import logging


class Locators(object):
    """ Локаторы страницы авторизации"""

    LOG_IN_BUTTON = (By.CSS_SELECTOR, '.header__sign_up')  # Кнопка логин в шапке сайта
    MAIL_LOG_IN = (By.CSS_SELECTOR, '.popup .login__input')  # Поле ввода почты на открывшемся поп-апе
    PASSWORD = (By.CSS_SELECTOR, '.popup .login__input[type="password"]')  # Поле ввода пароля на открывшемся поп-апе
    AUTH_BTN = (By.CSS_SELECTOR, '.login--button')  # Кнопка авторизации
    POP_UP = (By.CSS_SELECTOR, '.login-container')  # Окно авторизации
    HEADER = (By.CSS_SELECTOR, '.header__nav')  # Шапка страницы после авторизации




class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Авторизация или регистрация пользователя"""

    def login(self, mail, password):
        """Авторизация"""

        time.sleep(1)
        login_btn = self.driver.find_element(*Locators.LOG_IN_BUTTON)
        time.sleep(1)
        login_btn.click()
        logging.info('Открытие окна авторизации...')

        # pop_up = self.driver.find_element(*Locators.POP_UP)
        pop_up = Locators.POP_UP
        GBtool.check_exists_by_css(self, css=pop_up[1], name='Окно авторизации')

        mail_lgn = self.driver.find_element(*Locators.MAIL_LOG_IN)
        time.sleep(1)
        mail_lgn.click()
        logging.debug('Ввод почты...')
        mail_lgn.send_keys(mail)


        psswrd = self.driver.find_element(*Locators.PASSWORD)
        psswrd.click()
        psswrd.send_keys(password)
        logging.info("Ввод пароля...")

        auth_btn = self.driver.find_element(*Locators.AUTH_BTN)
        auth_btn.click()
        logging.info('Авторизация...')

        time.sleep(1)
        # header = self.driver.find_element(*Locators.HEADER)
        header = Locators.HEADER
        time.sleep(1)
        GBtool.check_exists_by_css(self, css=header[1], name='Шапка после регистрации')
        logging.info('Авторизация прошла успрешно.')











