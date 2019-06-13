import unittest
from selenium import webdriver
from under_the_hood.log_in_page import MainPage
from under_the_hood import My_oders
from under_the_hood.multyusable import GBtool
from under_the_hood.Top_boosters import TopBoostPage
from under_the_hood.Constructor import Constructor
import time



class TopBoostersPage(unittest.TestCase):

    mail = 'autotest@nooders.ru'
    password = '98flow'
    mail2 = 'second@customer.ru'

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        self.driver.get("https://dev.gamersbay.com/")
        main_page = MainPage(self.driver)
        main_page.login(self.mail, self.password)

    def test_01_download_no_orders(self):
        """ЗАгрузка дэшборда, с профиля без заказов, октрытого из разных вкладок"""

        gb_tool = GBtool(self.driver)
        top_boost = TopBoostPage(self.driver)

        # gb_tool.goto_tab(home=True)
        time.sleep(1)
        gb_tool.go_to_menu('BALANCE')
        top_boost.check_components()

        gb_tool.goto_tab(my_orders=True)
        time.sleep(1)
        gb_tool.goto_tab(top_boost=True)
        top_boost.check_components()

        gb_tool.goto_tab(popular=True)
        time.sleep(1)
        gb_tool.goto_tab(top_boost=True)
        top_boost.check_components()

    def test_02_download_with_orders(self):
        """Загрузка дэщбоарда с профиля с заказами, открытого из разных вкладок"""

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()