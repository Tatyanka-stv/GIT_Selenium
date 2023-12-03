import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://estro.ua/login")
    phone_input = driver.find_element(By.NAME, "phone_number")
    password_input = driver.find_element(By.NAME, "password")
    phone_input.send_keys("0992276228")
    password_input.send_keys("qa32")
    password_input.send_keys(Keys.RETURN)
    
    time.sleep(10)

    # Отримуємо URL сторінки після авторизації
    current_url = driver.current_url

    # Перевіряємо, чи користувач був успішно авторизований
    if "login" not in current_url:
        print("Успішно авторизовано")
    else:
        print("Помилка авторизації")  
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()



