from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# locate Amazon Logo
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

#Locate Create Account
driver.find_element(By.CSS_SELECTOR, '.a-spacing-small')

#Locate "Your Name" field
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#Locate "email" field
driver.find_element(By.CSS_SELECTOR, '#ap_email')

#Locate "Password" field
driver.find_element(By.CSS_SELECTOR, '#ap_password')

#Locate "Re-enter password" field
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#Locate "Create your Amazon account" button (changed to "continue button)
driver.find_element(By.CSS_SELECTOR, '#continue')

#Locate "Conditions of Use" text
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_condition_of_use']")

#Locate "Privacy Notice" text
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_privacy_notice']")

#Locate "Sign in" text (at bottom of page)
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')

