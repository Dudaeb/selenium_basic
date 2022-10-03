import time
from selenium import webdriver
class Crome():
    def crome(self):
        driver = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://www.google.com/")
        driver.get("https://www.youtube.com/watch?v=fDhycv7KwKY&list=RDfDhycv7KwKY&start_radio=1")
        time.sleep(1000)
        driver.close()

test_obkec = Crome()
test_obkec.crome()
