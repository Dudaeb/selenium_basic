import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
time.sleep(3)
Email= driver.find_element(By.ID, "Email")
Email.clear()
time.sleep(3)
Email.send_keys("admin@yourstore.com")
time.sleep(3)
pass1=driver.find_element(By.ID, "Password")
pass1.clear()
time.sleep(3)
pass1.send_keys("admin")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "[class='button-1 login-button']").click()
time.sleep(3)