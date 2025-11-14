from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# inspect -> href = Link type botton

print('test start')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.calculator.net/')
BMI_Calc = driver.find_element(By.LINK_TEXT,'BMI Calculator')
BMI_Calc.click()

current_url = driver.current_url
print(f'current URL is {current_url}')

health_button = driver.find_element(By.PARTIAL_LINK_TEXT,"FITNESS")
health_button.click()
health_button = driver.current_url
print(f'Health page URL is {current_url}')

driver.close()

print("Test end - success")