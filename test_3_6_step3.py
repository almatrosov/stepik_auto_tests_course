import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('lessons', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestStrangePage():
    def test_form(self, browser, lessons):
        link = f"https://stepik.org/lesson/{lessons}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)
        input = browser.find_element(By.TAG_NAME, "textarea")
        answer = math.log(int(time.time()))
        input.send_keys(answer)
        button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
        button.click()
        browser.implicitly_wait(10)
        correct_msg_tag = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
        correct_msg = correct_msg_tag.text
        if correct_msg != 'Correct!':
            print(correct_msg)
        assert correct_msg == 'Correct!', "Your input is incorrect"