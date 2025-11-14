from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print('Test start')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.nike.com/il/')
woman = driver.find_element(By.LINK_TEXT , 'Women')
if woman:
    print('Women link found')
else:
    print('Women link NOT found')
men = driver.find_element(By.LINK_TEXT , 'Men')
if men:
    print('Men link found')
else:
    print('Men link NOT found')

driver.close()

print("Test end - success")