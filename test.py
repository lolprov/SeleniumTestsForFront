from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path='./chromedriver.exe')
driver = webdriver.Chrome(service=service)
try:
    driver.maximize_window()
    driver.get('http://localhost:3000')
    time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()