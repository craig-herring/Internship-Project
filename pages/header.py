from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN = (By.ID, 'account-sign-in')
    SIDE_NAV_CLICK_SIGN_IN = (By.XPATH, "//*[@data-test='accountNav-signIn']")

    def search(self, text):
        print(f'Searching for {text}')
        self.input_text(text, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_sign_in(self):
        self.click(*self.SIGN_IN)

    def side_nav_click_sign_in(self):
            self.click(*self.SIDE_NAV_CLICK_SIGN_IN)