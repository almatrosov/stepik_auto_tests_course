from selenium.webdriver.common.by import By

class TestGoodsPage():
    def test_cart_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        browser.implicitly_wait(10)
        button = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form")
        assert button, "Жесть! Кнопка добавления в корзину не найдена!"