from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print("Test start")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://demo.applitools.com/#')
user = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")
login_button = driver.find_element(By.ID,'log-in')

user.send_keys('user')
password.send_keys('sauce')
login_button.click()

driver.close()
print("Test end - success")