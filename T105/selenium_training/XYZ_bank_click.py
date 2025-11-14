from selenium.webdriver.common.by import By
from T105.selenium_training.selenium_base import seleniumBase105

base = seleniumBase105()
driver = base.selenium_start_with_url('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')

buttons = driver.find_elements(By.CLASS_NAME,"btn.btn-primary.btn-lg")
buttons[1].click()

base.selenium_end()