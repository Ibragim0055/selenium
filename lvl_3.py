from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = wd.Chrome(options=options)
driver.get('https://uzum.uz/ru')

button = driver.find_elements(By.CLASS_NAME, 'product-wrapper')


print(button)

for i in button:
    print(i.text)