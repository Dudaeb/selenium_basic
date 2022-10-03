from selenium import webdriver
class Firefox():
    def firefox(self):
        driver = webdriver.Firefox(executable_path="C:\\Driver\\geckodriver-v0.31.0-win64\\geckodriver.exe")
        driver.get("http://www.tutorialsninja.com/demo")
        driver.find_element_by_name("search").send_keys("iphone")

afd = Firefox()
afd.firefox()
