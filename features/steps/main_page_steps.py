from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")


@given('Open target main page')
def open_target_main(context):
    context.app.main_page.open_main_page()


@given('Open sign in page')
def click_sign_in(context):
    context.app.header.click_sign_in()
    sleep(1)

@when('Click Sign In')
def click_sign_in(context):
    context.app.header.click_sign_in()
    sleep(1)


@when('From right side navigation menu, click Sign In')
def side_nav_click_sign_in(context):
    context.app.header.side_nav_click_sign_in()
    sleep(4)


@then('Verify Sign In form opened')
def verify_Sign_In_page_opens(context):
    context.app.main_page.verify_Sign_In_form_opens()


@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search(search_word)


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()


@then('Verify at least 1 link shown')
def verify_1_header_link_shown(context):
    link = context.driver.find_element(*HEADER_LINKS)
    print(link)
    # Stale Element Reference Ex
    # print("Before refresh:", link)
    # context.driver.refresh()
    # link = context.driver.find_element(*HEADER_LINKS)
    # link.click()
    # print("AFTER refresh:", link)


@then('Verify {link_amount} links shown')
def verify_all_header_links_shown(context, link_amount):
    link_amount = int(link_amount) #"6" => int 6
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == link_amount, f'Expected {link_amount} links, but got {len(links)}'


