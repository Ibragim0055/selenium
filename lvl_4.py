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
    a = i.find_element(By.XPATH, './/span[@data-test-id="text__price"]')
    b = i.find_element(By.XPATH, './/span[@data-test-id="text__old-price"]')
    print(f'Цена сейчас: {a.text}\nЦена раньше: {b.text}')