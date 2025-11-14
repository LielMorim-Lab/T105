from selenium.webdriver.common.by import By
from T105.selenium_training.selenium_base import seleniumBase105

base = seleniumBase105()
driver = base.selenium_start()

driver.get('https://www.ebay.com/')
driver.find_element(By.LINK_TEXT,'Advanced').click()
title_desc = driver.find_element(By.NAME,'LH_TitleDesc')
# == driver.find_element(By.NAME,'LH_TitleDesc').click()

before = title_desc.is_selected()
# .is_selected() automatic response is True / False only with checkbox
print(f'the status before is {before}')
if not before:
    title_desc.click()

title_desc.click()

after = title_desc.is_selected()
print(f'the status after is {after}')

base.selenium_end()