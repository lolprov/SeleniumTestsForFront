import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

webdriver_path = './chromedriver.exe'
server_location = 'http://localhost:3000'


def init_driver():
    service = Service(executable_path=webdriver_path)
    driver = webdriver.Chrome(service=service)
    return driver


class TestSelenium(unittest.TestCase):

    def test_site_name_check(self) -> None:
        driver = init_driver()
        driver.get(server_location)

        self.assertTrue("Unleash Your Wishlist" in driver.page_source)
        driver.close()

    def test_login_name_check(self) -> None:
        driver = init_driver()
        driver.get(server_location)

        self.assertTrue("login" in driver.page_source)
        driver.close()

    def test_create_wishlist_check_name(self) -> None:
        driver = init_driver()
        driver.get(server_location)

        self.assertTrue("Create Wishlist" in driver.page_source)
        driver.close()
