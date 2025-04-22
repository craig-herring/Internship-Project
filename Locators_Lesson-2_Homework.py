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

# Email field
driver.find_element(By.ID, 'ap_email')

#Continue button
driver.find_element(By.ID, 'continue')

#Conditions of Use link
driver.find_element(By.ID, 'legalTextRow')

#Privacy Notice link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#Need Help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#Forgot Your Password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#Other Issues with Sign-in link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

#Create Your Amazon Account button
driver.find_element(By.ID, 'createAccountSubmit')




