import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.NAME, 'username').send_keys('Admin')
time.sleep(5)
driver.find_element(By.NAME, 'password').send_keys('admin123')
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, '.orangehrm-login-button').click()
time.sleep(5)
driver.close()