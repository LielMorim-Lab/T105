from selenium.webdriver.common.by import By

from T105.String_example import counter
from T105.selenium_training.selenium_base import seleniumBase105

base = seleniumBase105()
driver = base.selenium_start_with_url('https://www.saucedemo.com/')

user = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.NAME,"password")
login_button = driver.find_element(By.ID,'login-button')

user.send_keys('standard_user')
password.send_keys('secret_sauce')

login_button.click()

first_price = driver.find_element(By.CLASS_NAME,'inventory_item_price')
price = first_price.text
print(f' the price is {price}')

all_Prices = driver.find_elements(By.CLASS_NAME,'inventory_item_price')
counter = 0
for price in all_Prices:
    text_price = price.text
    counter += 1
    print(f'{counter} - the price found with value {text_price}')

base.selenium_end()