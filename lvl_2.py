from selenium import webdriver as wd
from selenium.webdriver.common.by import By


driver = wd.Chrome()
driver.get('https://selectel.ru/blog/?utm_source=habr.com&utm_medium=referral&utm_campaign=parsing_150823_academy')

a = driver.find_element(By.CLASS_NAME, 'header_search')
a.click()

b = driver.find_element(By.CLASS_NAME, 'search-modal_input')
b.send_keys('python')


