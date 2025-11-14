import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print("Test start")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.saucedemo.com/') # get = go to URL
user = driver.find_element(By.ID,"user-name") # inspect -> elements -> id
# user1= driver.find_element(By.ID,"user-name")
password = driver.find_element(By.NAME,"password")
# pw = driver.find_element(By.ID,"password")
login_button = driver.find_element(By.ID,'login-button')

user.send_keys('standard_user') # send_keys = type value
password.send_keys('secret_sauce')
login_button.click()

time.sleep(3) # if you use time.sleep(3) you need to add a line that says import time
driver.close() #driver.quit() same as driver.close()

print("Test end - success")