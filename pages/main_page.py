from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')

    def open_main_page(self):
        self.open_url(self.base_url)
        self.wait_until_clickable(*self.SEARCH_FIELD)

    def verify_Sign_In_page_opens(self):
        self.verify_url(f'{self.base_url}sign_in_page')  # 'https://www.target.com/' + 'cart'