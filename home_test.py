import unittest
from selenium import webdriver
from under_the_hood.log_in_page import MainPage
from under_the_hood.Home_page import HomePage
from under_the_hood.multyusable import GBtool
import time




class HomePageNoOders(unittest.TestCase):

    mail = 'autotest@nooders.ru'
    password = '98flow'

    mail2 = 'second@customer.ru'

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        self.driver.get("https://dev.gamersbay.com/")
        main_page = MainPage(self.driver)
        main_page.login(self.mail, self.password)

    def test_01_no_order_dowload(self):
        """Проверка перехода на домашнюю страницу со страницы пользователя без заказов """

        home_page = HomePage(self.driver)
        #  home_page.goto()
        home_page.check_components_bosoter_no_oders()


    def tearDown(self):
        self.driver.close()


class HomePageWithOrders(unittest.TestCase):

    mail = 'second@customer.ru'
    password = '98flow'

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        self.driver.get("https://dev.gamersbay.com/")
        main_page = MainPage(self.driver)
        main_page.login(self.mail, self.password)

    def test_01_with_orders_download(self):
        """Проверка перехода на домашнюю странциу со всех вкладок"""

        gbtools = GBtool(self.driver)
        home_page = HomePage(self.driver)

        gbtools.go_to_tab_booster(my_orders=True)
        time.sleep(1)
        gbtools.go_to_tab_booster(home=True)
        home_page.check_components_with_order()

        gbtools.goto_tab(auto=True)
        gbtools.goto_tab(home=True)
        home_page.check_components_with_order()

        gbtools.goto_tab(top_boost=True)
        gbtools.goto_tab(home=True)
        home_page.check_components_with_order()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()