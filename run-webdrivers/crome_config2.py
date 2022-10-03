import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.google.com/search?q=")
time.sleep(60)
driver.close()