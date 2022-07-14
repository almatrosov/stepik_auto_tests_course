import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegForm(unittest.TestCase):
    def test_RegForm1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        input3.send_keys("almatrosov@yandex.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be absolute value of a number")

    def test_RegForm2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        input3.send_keys("almatrosov@yandex.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be absolute value of a number")

if __name__ == "__main__":
	unittest.main()