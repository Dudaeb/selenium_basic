import time
from selenium import webdriver
class Edge():
    def edge(self):
        driver = webdriver.Edge(executable_path="C:\\Driver\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://www.facebook.com/")
        driver.get("https://www.youtube.com/watch?v=fDhycv7KwKY&list=RDfDhycv7KwKY&start_radio=1")
        time.sleep(100)
        driver.close()


dfdsf = Edge()
dfdsf.edge()
