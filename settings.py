import unittest
from selenium import webdriver
from under_the_hood.log_in_page import MainPage
from under_the_hood import My_oders
from under_the_hood.multyusable import GBtool
from under_the_hood.Settings import Settings
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

    def test_01_download(self):
        """ЗАгрузка баланса, октрытого из разных вкладок"""

        gb_tool = GBtool(self.driver)
        settings = Settings(self.driver)



        time.sleep(1)
        gb_tool.go_to_menu('SETTINGS')
        settings.check_components()

        gb_tool.goto_tab(my_orders=True)
        time.sleep(1)
        gb_tool.go_to_menu('SETTINGS')
        settings.check_components()

        gb_tool.goto_tab(popular=True)
        time.sleep(1)
        gb_tool.go_to_menu('SETTINGS')
        settings.check_components()

        gb_tool.goto_tab(top_boost=True)
        time.sleep(1)
        gb_tool.go_to_menu('SETTINGS')
        settings.check_components()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()