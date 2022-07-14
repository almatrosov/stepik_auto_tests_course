from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "input_value")
    y = calc(x.text)
    browser.execute_script("window.scrollBy(0, 100);")
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']")
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")
    radio.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()