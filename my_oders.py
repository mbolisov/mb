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
    mail2 = 'second@customer.ru'

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

    # def test_02_tab_download(self):
    #     """Проверка загрузки вкладки, открытой из разных вкладок"""
    #
    #     gb_tool = GBtool(self.driver)
    #     my_orders = MyOdersPage(self.driver)
    #
    #     gb_tool.goto_tab(home=True)
    #     time.sleep(1)
    #     gb_tool.goto_tab(my_orders=True)
    #     my_orders.check_components_with_orders()
    #
    #     gb_tool.goto_tab(popular=True)
    #     time.sleep(1)
    #     gb_tool.goto_tab(my_orders=True)
    #     my_orders.check_components_with_orders()
    #
    #     gb_tool.goto_tab(top_boost=True)
    #     time.sleep(1)
    #     gb_tool.goto_tab(my_orders=True)
    #     my_orders.check_components_with_orders()

    def test_03_new_order(self):
        """Проверка работы кнопок создания заказа"""

        gb_tool = GBtool(self.driver)
        my_orders = My_oders(self.driver)
        constructor = Constructor(self.driver)

        gb_tool.goto_tab(my_orders=True)
        btn = my_orders.Locators.NEW_ORDER_BTN_LEFT(self.driver)
        btn = self.driver.find_element_by_css_selector(btn)
        btn.click()
        constructor.is_constructor_download()

        gb_tool.goto_tab(my_orders=True)
        btn2 = my_orders.Locators.NEW_ORDER_BTN_RIGHT(self.driver)
        btn2 = self.driver.find_element_by_css_selector(btn2)
        btn2.click()
        constructor.is_constructor_download()
    #
    # def test_04_sorting(self):
    #     """Проверка сортирвоки вкладки"""
    #
    #     gb_tool = GBtool(self.driver)
    #     my_orders = My_oders(self.driver)
    #
    #     gb_tool.relog(log=self.mail2, pswrd=self.password)
    #     gb_tool.goto_tab(my_orders=True)
    #
    #     game_list = ['all games', 'World of Warcraft', 'Counter-Strike', 'Overwatch', 'Dota 2', 'League of legends']
    #     i = 1
    #     while i < len(game_list):
    #
    #         my_orders.do_sort_by_game(game_list[i])
    #         i += 1
    #
    #     cat_list = ['All orders', 'Auction', 'In progress', 'Waiting', 'Warranty', 'Done', 'Drafts']
    #     i = 1
    #     while i < len(cat_list):
    #
    #         my_orders.do_sort_by_cat(cat_list[i])
    #         i += 1

    # def test_05(self):
    #     """ Проверка открытия чата """

        #Допишу после создания тестового акка

    def tearDown(self):
        self.driver.close()

class MyOdersWithOders(unittest.TestCase):
    """Тесты вкладки мои заказы под аккаунтами с заведенными заказами"""


    mail = 'autotest@nooders.ru'
    password = '98flow'
    mail2 = 'second@customer.ru'

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        self.driver.get("https://dev.gamersbay.com/")
        main_page = MainPage(self.driver)
        main_page.login(self.mail2, self.password)

    def test_01_tab_download(self):
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

    def test_02_sorting(self):
        """Проверка сортирвоки вкладки"""

        gb_tool = GBtool(self.driver)
        my_orders = My_oders(self.driver)

        gb_tool.goto_tab(my_orders=True)

        game_list = ['all games', 'World of Warcraft', 'Counter-Strike', 'Overwatch', 'Dota 2', 'League of legends']
        i = 1
        while i < len(game_list):
            my_orders.do_sort_by_game(game_list[i])
            i += 1

        cat_list = ['All orders', 'Auction', 'In progress', 'Waiting', 'Warranty', 'Done', 'Drafts']
        i = 1
        while i < len(cat_list):
            my_orders.do_sort_by_cat(cat_list[i])
            i += 1

    def test_03(self):
        """ Проверка открытия чата """

        # Допишу после создания тестового акка

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()