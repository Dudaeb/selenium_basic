from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F&fbclid=IwAR3WGKGkhIvbbA4XS83NPghg2CXcKu5Y7TB5sISMT2ctjYuqjjpn0Yt4MlU")
time.sleep(3)

input_email=driver.find_element(By.NAME, "Email")
input_email.clear()
time.sleep(3)
input_email.send_keys("admin@yourstore.com")
time.sleep(3)
input_pass=driver.find_element(By.NAME, "Password")
input_pass.clear()
time.sleep(3)
input_pass.send_keys("admin")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "[class='button-1 login-button']").click()
time.sleep(3)





