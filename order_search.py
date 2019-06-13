import unittest
from selenium import webdriver
from under_the_hood.log_in_page import MainPage
from under_the_hood import My_oders
from under_the_hood.multyusable import GBtool
from under_the_hood.booster.Order_search import OrderSearch
from under_the_hood.booster.Order_search import Locators
from under_the_hood.Constructor import Constructor
import time



class TopBoostersPage(unittest.TestCase):

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
        ordrs =  OrderSearch(self.driver)

        gbtools.go_to_tab_booster(my_orders=True)
        time.sleep(1)
        gbtools.go_to_tab_booster(search_orders=True)
        ordrs.check_components()

        gbtools.go_to_tab_booster(auto=True)
        gbtools.go_to_tab_booster(search_orders=True)
        ordrs.check_components()

        gbtools.go_to_tab_booster(top_boost=True)
        gbtools.go_to_tab_booster(search_orders=True)
        ordrs.check_components()

    def test_02_sort(self):
        """Сортировка"""

        gb_tools = GBtool(self.driver)
        ordrs = OrderSearch(self.driver)

        gb_tools.go_to_tab_booster(search_orders=True)
        gb_tools.do_sort_by_game('World of Warcraft')
        gb_tools.check_sort_service_boost()
        ordrs.check_sort_by_service()
        ordrs.lang_checker(eng=True)

    def test_03_place_bid(self):
        """Работа кнопки кинуть ставку"""

        ordrs = OrderSearch(self.driver)
        gb_tools = GBtool(self.driver)
        gb_tools.go_to_tab_booster(search_orders=True)
        time.sleep(5)
        order = self.driver.find_elements(*Locators.ORDER)[0]
        show_more = order.find_element(*Locators.SHOW_MORE)
        place_bid = order.find_element(*Locators.PLACE_BID)
        show_more.click()
        gb_tools.check_exists_by_css(css='.btn--primary', name='сделать ставку')
        place_bid.click()
        bid = self.driver.find_element(*Locators.STAVOCHKA)
        gb_tools.check_exists_by_css(css='.bid', name='форма ставки')


    def test_04_delete(self):
        """Удалить ставку"""

        ordrs = OrderSearch(self.driver)
        gb_tools = GBtool(self.driver)
        gb_tools.go_to_tab_booster(search_orders=True)
        time.sleep(5)
        ordrs.delete()

    def test_05_fav(self):
        """добавление заказа в избранные"""





def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()