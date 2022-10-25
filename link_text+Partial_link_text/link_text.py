import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager



class Link_text():
    def linl_text(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get("https://www.youtube.com/")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Library").click()

test_object=Link_text()
test_object.linl_text()