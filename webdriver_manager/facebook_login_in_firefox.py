from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(3)

driver.find_element(By.NAME, "email").send_keys("@gmail.com")
time.sleep(3)
driver.find_element(By.NAME, "pass").send_keys("100")
time.sleep(3)
driver.find_element(By.NAME, "login").click()
time.sleep(3)

