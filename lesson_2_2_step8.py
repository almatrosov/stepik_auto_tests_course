from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")
    input1.send_keys("Alexus")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']")
    input2.send_keys("Popov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    input3.send_keys("popov@yandex.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lol.txt')
    upload = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    upload.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()