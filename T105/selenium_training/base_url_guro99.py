from selenium.webdriver.common.by import By
from T105.selenium_training.selenium_base import seleniumBase105

base = seleniumBase105() # (instance)
driver = base.selenium_start_with_url('https://demo.guru99.com/test/newtours/index.php') # (function)

driver.find_element(By.NAME,'userName').send_keys('tutorial')
driver.find_element(By.NAME,'password').send_keys('tutorial')
driver.find_element(By.NAME,'submit').click()
print('Log in was successful')

base.selenium_end()