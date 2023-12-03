from selenium import webdriver
import time

# Ініціалізація веб-драйвера 
driver = webdriver.Chrome()

try:

    # Відкриття сторінки
    driver.get("https://www.selenium.dev/")
    # Отримання заголовка сторінки
    page_title = driver.title
    time.sleep(5)
    # Виведення заголовка сторінки
    print("Заголовок сторінки:", page_title)
except Exception as ex:
    print(ex)
finally:
    # Закриття веб-драйвера
    driver.close()
    driver.quit()

