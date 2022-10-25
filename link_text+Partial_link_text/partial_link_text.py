import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager



class Partial_Link_text():
    def partial_link_text(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get("https://www.youtube.com/")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.PARTIAL_LINK_TEXT, "Libr").click()

test_object=Partial_Link_text()
test_object.partial_link_text()