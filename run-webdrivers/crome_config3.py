from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
abc = Service("C:\\Driver\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=abc)

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