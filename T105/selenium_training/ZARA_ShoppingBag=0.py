from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print(' ')

print('Test start')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.zara.com/il/en/')
shoping_bag = driver.find_element(By.PARTIAL_LINK_TEXT,'SHOPPING BAG')
shoping_bag_text = shoping_bag.text

if shoping_bag_text == 'SHOPPING BAG [0]':
    print('shopping bag is empty')
else:
    print("shoping bag isn't empty")

print('Test End - Success')

driver.close()