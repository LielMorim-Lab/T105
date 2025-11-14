from selenium.webdriver.common.by import By
from T105.selenium_training.selenium_base import seleniumBase105
base = seleniumBase105()
driver = base.selenium_start()

driver.get('https://www.ebay.com/')
Advanced = driver.find_element(By.LINK_TEXT,'Advanced')
Adv_text = Advanced.text

print(f'the text is "{Adv_text}"')
Advanced.click()

print(f'URL is {driver.current_url}')

base.selenium_end()