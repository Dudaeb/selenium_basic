from selenium import webdriver

class Firefox():
    def firefox(self):
        driver = webdriver.Firefox(executable_path="C:\\Driver\\geckodriver-v0.31.0-win64\\geckodriver.exe")
        driver.get("https://www.youtube.com/watch?v=fDhycv7KwKY&list=RDfDhycv7KwKY&start_radio=1")


test_object = Firefox()
test_object.firefox()
