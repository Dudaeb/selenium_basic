import time
from  selenium import webdriver
driver = webdriver.Firefox(executable_path="C:\\Driver\\geckodriver-v0.31.0-win64\\geckodriver.exe")

driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(10)
driver.get("https://www.facebook.com")
time.sleep(10)
driver.get("https://www.youtube.com")
driver.minimize_window()
time.sleep(10)
driver.close()