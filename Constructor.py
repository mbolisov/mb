from selenium.webdriver.common.by import By
from under_the_hood.multyusable import GBtool
import logging


class Locators(object):

    CONSTRUCTOR = (By.CSS_SELECTOR, '.constructor--')
    NEW_ORDER = (By.CSS_SELECTOR, '.header__new-order-btn')  # Кнопка новый заказ


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class Constructor(BasePage):

    def is_constructor_download(self):

        gb_tool = GBtool(self.driver)


        download = gb_tool.check_exists_by_css(css=Constructor[1], name='Конструктор')

        assert download == True('Констурктор не загрузился')

        print('Конструктор загружен')

    def open(self):

        gb_tool = GBtool(self.driver)


        new_btn = self.driver.find_element(*Locators.NEW_ORDER)
        new_btn.click()

        constructor = self.driver.find_element(*Locators.CONSTRUCTOR)
        gb_tool.check_exists_by_css(css=constructor, name="Конструктор")









