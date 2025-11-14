from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print('Test start')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.ebay.com/')
search = driver.find_element(By.ID,'gh-ac')
search.send_keys('book')
search.send_keys(Keys.ENTER)

driver.close()

print("Test end - success")