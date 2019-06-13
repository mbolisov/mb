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

    def test_01_download(self):
        """ЗАгрузка вкладки топ бустеры, октрытой из разных вкладок"""

        gb_tool = GBtool(self.driver)
        top_boost = TopBoostPage(self.driver)

        # gb_tool.goto_tab(home=True)
        time.sleep(1)
        gb_tool.goto_tab(top_boost=True)
        top_boost.check_components()

        gb_tool.goto_tab(my_orders=True)
        time.sleep(1)
        gb_tool.goto_tab(top_boost=True)
        top_boost.check_components()

        gb_tool.goto_tab(popular=True)
        time.sleep(1)
        gb_tool.goto_tab(top_boost=True)
        top_boost.check_components()

    def test_02_sort(self):
        """Сортировка раздела"""


        gb_tool = GBtool(self.driver)
        top_boost = TopBoostPage(self.driver)

        gb_tool.goto_tab(top_boost=True)
        gb_tool.do_sort_by_game('World of Warcraft')
        top_boost.check_sort_by_service()
        top_boost.search_check('secondbooster')

    def test_03(self):
        """Инвайт - дезинвайт"""


        gb_tool = GBtool(self.driver)
        gb_tool.goto_tab(top_boost=True)
        top_boost = TopBoostPage(self.driver)
        top_boost.invite_booster()
        top_boost.dezinvite_boost()


        # while i < len(game_list):
        #     gb_tool.do_sort_by_game(game_list[i])
        #     i += 1

        # cat_list = ['All orders', 'Auction', 'In progress', 'Waiting', 'Warranty', 'Done', 'Drafts']
        # i = 1
        # while i < len(cat_list):
        #     gb_tool.do_sort_by_cat(cat_list[i])
        #     i += 1




    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()