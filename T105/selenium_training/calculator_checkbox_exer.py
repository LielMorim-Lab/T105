from selenium.webdriver.common.by import By
from T105.selenium_training.selenium_base import seleniumBase105

base = seleniumBase105()
driver = base.selenium_start()

driver.get('https://www.calculator.net/')

driver.find_element(By.LINK_TEXT,'Password Generator').click()
driver.find_element(By.ID,'ilower').submit()
# driver.find_element(By.ID,'ilower').click()
driver.find_element(By.ID,'iupper').submit()
driver.find_element(By.ID,'iexclude').submit()
driver.find_element(By.NAME,'submit1').submit()

base.selenium_end()