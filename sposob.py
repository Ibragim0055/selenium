#Закрытия рекламы
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "close_modal_window"))).click()


