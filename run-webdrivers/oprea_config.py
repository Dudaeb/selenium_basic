from selenium import webdriver
class Opera():
    def opera(self):
        driver = webdriver.opera(executable_path="C:\\Driver\\operadriver_win64\\operadriver.exe")
        driver.get("https://www.youtube.com/")



test_object = Opera()
test_object.opera()
