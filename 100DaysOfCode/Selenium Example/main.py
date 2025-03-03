from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org/")

dates_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget li time")
event_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events_dict = {}
for index in range(len(dates_list)):
    events_dict[index] = {
        'time': dates_list[index].text,
        'name': event_list[index].text
    }
print(events_dict)

driver.quit()



