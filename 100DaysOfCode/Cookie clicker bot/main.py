# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import time
#
# GAME_URL = "https://orteil.dashnet.org/experiments/cookie/"
# MINUTES_RUNNING_TIME = 5
#
#
# options = Options()
# options.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options)
#
# driver.get(GAME_URL)
#
#
# def buy_upgrades():
#     for store_item in store[-2::-1]:
#         price = store_item.find_element(By.TAG_NAME, 'b').text.split('-')[1].strip()
#         price = int(price.replace(",", ''))
#         current_money = int(money.text.replace(',',''))
#         if current_money >= price:
#             upgrade_id = store_item.get_attribute("id")
#             upgrade_to_buy = driver.find_element(By.ID, upgrade_id)
#             upgrade_to_buy.click()
#
#
# timeout = time.time() + 60*MINUTES_RUNNING_TIME
# last_update_time = time.time()
# while True:
#     money = driver.find_element(By.ID, "money")
#     cookie = driver.find_element(By.ID, "cookie")
#     store = driver.find_elements(By.CSS_SELECTOR, "#store div")
#     cookie.click()
#
#     if time.time() >= (last_update_time + 5):
#         buy_upgrades()
#         last_update_time = time.time()
#
#     if time.time() > timeout:
#         break
#
# driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(By.ID, 'cookie')

# Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
        