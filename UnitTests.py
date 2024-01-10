import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

webdriver_path = './chromedriver.exe'
server_location = 'http://localhost:3000'


class TestSelenium(unittest.TestCase):
    def test_site_name_check(self) -> None:
        service = Service(executable_path=webdriver_path)
        driver = webdriver.Chrome(service=service)
        driver.get(server_location)

        self.assertTrue("Unleash Your Wishlist" in driver.page_source)

        driver.close()