from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#  self = lets access an object’s variables in another function

class seleniumBase105(): # base = seleniumBase105() == instance

    def selenium_start (self) -> WebDriver:
        print("Test start")

        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver

    def selenium_end (self):
        self.driver.close()
        print("Test End - Success")

    def selenium_start_with_url (self, url):
        print("Test start")

        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        return self.driver
