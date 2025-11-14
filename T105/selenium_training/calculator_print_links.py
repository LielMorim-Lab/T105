from selenium.webdriver.common.by import By
from T105.selenium_training.selenium_base import seleniumBase105

base = seleniumBase105()
driver = base.selenium_start_with_url('https://www.calculator.net/')

links = driver.find_elements(By.PARTIAL_LINK_TEXT, 'Calculator')
counter = 0
for link in links:
    counter += 1
    print( f'{counter} - {link.text}')

base.selenium_end()