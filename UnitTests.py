import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

webdriver_path = './chromedriver.exe'
server_location = 'http://localhost:3000'


def init_driver():
    service = Service(executable_path=webdriver_path)
    driver = webdriver.Chrome(service=service)
    return driver


class TestSelenium(unittest.TestCase):

    def test_site_name_check(self) -> None:
        # Start page location test
        driver = init_driver()
        driver.get(server_location)

        self.assertTrue("Unleash Your Wishlist" in driver.page_source)
        driver.close()

    def test_login_name_check(self) -> None:
        # Check availability of login button
        driver = init_driver()
        driver.get(server_location)

        self.assertTrue("login" in driver.page_source)
        driver.close()

    def test_create_wishlist_check_name(self) -> None:
        # Check availability of create wishlist button
        driver = init_driver()
        driver.get(server_location)

        self.assertTrue("Create Wishlist" in driver.page_source)
        driver.close()

    def test_redirect_to_login_page(self) -> None:
        # Functional testing of login button
        driver = init_driver()
        driver.get(server_location)

        login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div[1]/div/a[1]")
        login_button.click()

        self.assertTrue("Welcome to our Wishlist" in driver.page_source)
        self.assertTrue("Sign In" in driver.page_source)

        driver.close()

    def test_redirect_and_empty_login(self) -> None:
        # Functional testing of sign in button on sign in page
        driver = init_driver()
        driver.get(server_location)

        login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div[1]/div/a[1]")
        login_button.click()

        sign_in_button = driver.find_element(By.CLASS_NAME, "submit-button")
        sign_in_button.click()

        self.assertTrue("Username is a required field" in driver.page_source)
        self.assertTrue("Password is required" in driver.page_source)

    def test_double_redirect(self) -> None:
        # Functional testing of redirect button on two pages
        driver = init_driver()
        driver.get(server_location)

        login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div[1]/div/a[1]")
        login_button.click()

        back_button = driver.find_element(By.CLASS_NAME, "welcome-side__media")
        back_button.click()

        self.assertTrue("Unleash Your Wishlist" in driver.page_source)
