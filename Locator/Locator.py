from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://demo.nopcommerce.com/')
time.sleep(10)
driver.find_element(By.NAME, "q").send_keys("ipnone")
driver.find_element(By.CSS_SELECTOR, "[class='button-1 search-box-button']").click()
time.sleep(10)
