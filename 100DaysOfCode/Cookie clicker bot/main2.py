from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

GAME_URL = "https://orteil.dashnet.org/experiments/cookie/"
MINUTES_RUNNING_TIME = 5


options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options)


driver.get(GAME_URL)

store = driver.find_elements(By.CSS_SELECTOR, '#store div')
cookie = driver.find_element(By.ID, 'cookie')
money = driver.find_element(By.ID, 'money')


store_dict = {}
for store_item in store:
    store_item_id = store_item.get_attribute('id')

    price = store_item.find_element(By.CSS_SELECTOR, 'b').text
    if price != "":
        price = price.strip().split('-')[1]
        price = int(price.replace(',', ""))

    store_dict[price] = store_item_id

store_dict.popitem() #######################


time_limit = time.time() + 60*MINUTES_RUNNING_TIME
last_cycle_time = time.time()
while True:
    cookie.click()
    current_time = time.time()

    if current_time - last_cycle_time >= 5:
        current_money = int(money.text.replace(',',""))

        item_to_buy = None
        item_to_buy_id = ""
        for item_price, item_id in store_dict.items():
            if current_money >= item_price:
                item_to_buy_id = item_id

        item_to_buy = driver.find_element(By.ID, item_to_buy_id)
        item_to_buy.click()

        last_cycle_time = current_time
    elif current_time >= time_limit:
        break

driver.quit()