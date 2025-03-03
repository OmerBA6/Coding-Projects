from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options)


driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME, "fName")
first_name_input.send_keys("asdasd")

last_name_input = driver.find_element(By.NAME, "lName")
last_name_input.send_keys("asdasd")

email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("ascasf@email.com")

sign_up_button = driver.find_element(By.XPATH, '/html/body/form/button')
sign_up_button.click()

driver.quit()
