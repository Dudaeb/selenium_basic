from selenium import webdriver
driver = webdriver.Firefox(executable_path="C:\\Driver\\geckodriver-v0.31.0-win64\\geckodriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element_by_name("username").send_keys("Admin")
driver.find_element_by_name("password").send_keys("admin123")
driver.find_element_by_name("submit").click()

