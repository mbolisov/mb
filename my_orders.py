import unittest
from selenium import webdriver
from under_the_hood.log_in_page import MainPage
from under_the_hood import My_oders
from under_the_hood.multyusable import GBtool
from under_the_hood.booster.My_Orders import MyOrders
from under_the_hood.Constructor import Constructor
import time



class MyOdersPage(unittest.TestCase):

    mail = 'second@booster.ru'
    password = '98flow'
    mail2 = 'second@customer.ru'

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        self.driver.get("https://dev.gamersbay.com/")
        main_page = MainPage(self.driver)
        main_page.login(self.mail, self.password)

    def test_01_check(self):
        """Проверка загрузки"""

        gbtools = GBtool(self.driver)
        ordrs = MyOrders(self.driver)

        gbtools.go_to_tab_booster(search_orders=True)
        time.sleep(1)
        gbtools.go_to_tab_booster(my_orders=True)
        ordrs.check_components()

        gbtools.go_to_tab_booster(auto=True)
        gbtools.go_to_tab_booster(my_orders=True)
        ordrs.check_components()

        gbtools.go_to_tab_booster(top_boost=True)
        gbtools.go_to_tab_booster(my_orders=True)
        ordrs.check_components()

    def test_02_sort(self):
        """Проверка сортировки"""

        gb_tools = GBtool(self.driver)
        ordrs = MyOrders(self.driver)

        gb_tools.go_to_tab_booster(my_orders=True)
        time.sleep(1)
        ordrs.check_game()



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()