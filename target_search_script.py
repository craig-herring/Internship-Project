from selenium import webdriver
from selenium.webdriver import Keys
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
driver.get('https://www.target.com/')

driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(4)

#Verification
#driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']")
#print('test case passed')

#By checking text
actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
print('Actual text:\n', actual_text)

assert 'tea' in actual_text, f'Error. Text tea not in {actual_text}'
print('Test case passed')

#sleep(4)