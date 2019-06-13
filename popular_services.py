import unittest
from selenium import webdriver
from under_the_hood.log_in_page import MainPage
from under_the_hood import My_oders
from under_the_hood.multyusable import GBtool
from under_the_hood.My_oders import MyOdersPage
from under_the_hood.Constructor import Constructor
import time



class MyOrdersPageNoOders(unittest.TestCase):

    mail = 'autotest@nooders.ru'
    password = '98flow'

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        self.driver.get("https://dev.gamersbay.com/")
        main_page = MainPage(self.driver)
        main_page.login(self.mail, self.password)

    def test_01(self):
        """Проверка перехода на домашнюю страницу со страницы пользователя без заказов """

        gb_tool = GBtool(self.driver)
        my_orders = MyOdersPage(self.driver)

        gb_tool.goto_tab(my_orders=True)
        time.sleep(1)
        my_orders.check_components_no_orders()

        # *************************************** Вкладка не работает **************

    def test_02_tab_download(self):
        """Проверка загрузки вкладки, открытой из разных вкладок"""

        gb_tool = GBtool(self.driver)
        my_orders = MyOdersPage(self.driver)

        gb_tool.goto_tab(home=True)
        time.sleep(1)
        gb_tool.goto_tab(my_orders=True)
        my_orders.check_components_with_orders()

        gb_tool.goto_tab(popular=True)
        time.sleep(1)
        gb_tool.goto_tab(my_orders=True)
        my_orders.check_components_with_orders()

        gb_tool.goto_tab(top_boost=True)
        time.sleep(1)
        gb_tool.goto_tab(my_orders=True)
        my_orders.check_components_with_orders()