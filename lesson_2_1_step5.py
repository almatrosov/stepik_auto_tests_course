import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x_text = x_element.text
    y = calc(x_text)
    input = browser.find_element(By.TAG_NAME, "input")
    input.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']")
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()