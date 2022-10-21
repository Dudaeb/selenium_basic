from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
class Crome_cofig():
    def crome_config(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(15)
        driver.find_element(By.NAME, 'username').send_keys('Admin')
        time.sleep(15)
        driver.find_element(By.NAME, 'password').send_keys('admin123')
        time.sleep(15)
        driver.find_element(By.CSS_SELECTOR, '.orangehrm-login-button').click()
        time.sleep(15)
        driver.close()
test_object=Crome_cofig()
test_object.crome_config()