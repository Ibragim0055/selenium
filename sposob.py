#Закрытия рекламы
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "close_modal_window"))).click()

#Нажатия на клавишу Enter при поиска
wb_search.send_keys(Keys.ENTER)



#Чтобы не получать ошибку DevTools listening on ws://127.0.0.1
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = wd.Chrome(options=options)
