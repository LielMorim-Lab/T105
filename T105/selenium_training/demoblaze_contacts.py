from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print('test start')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.demoblaze.com')
Contact = driver.find_element(By.LINK_TEXT,'Contact')
Contact_text = Contact.text

if (Contact_text == 'Contact'):
    print('Contact text found')
    Contact.click()
else:
    print('No Contact found')

print('Test end - success')

driver.quit()