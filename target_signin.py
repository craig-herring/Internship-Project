from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Start Chrome browser
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

# open Target.com
driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

#Verification
expected = 'Sign into your Target account'
actual = driver.find_element(By.XPATH, "//h1[contains9@class, 'styles_ndsHeading')]").text
assert expected == actual, f'Expected {expected} did not match actual {actual}'

sleep(3)
