from selenium.webdriver.common.by import By

from pages.base_page import Page




class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    FAVORITES_BTN = (By.CSS_SELECTOR, ".[data-tests='FavoritesButton']")
    FAVORITES_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")

    def hover_fav_icon(self):
        fav_icon = self.find_element(*self.FAVORITES_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(fav_icon)
        actions.perform()


    def verify_search_results(self, expected_text):
        self.verify_partial_text(expected_text, *self.SEARCH_RESULTS_TEXT)

    def verify_results_url(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)

