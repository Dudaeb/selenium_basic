import time
from  selenium import webdriver
driver = webdriver.Firefox(executable_path="C:\\Driver\\geckodriver-v0.31.0-win64\\geckodriver.exe")

driver.maximize_window()
driver.get("https://www.google.com/")
print(driver.title)
time.sleep(10)
driver.get("https://www.facebook.com")
print(driver.title)
time.sleep(10)
driver.get("https://www.youtube.com")
print(driver.title)
driver.minimize_window()
time.sleep(10)
driver.close()