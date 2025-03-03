import requests
import itertools

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = ""
ALPHA_VANTAGE_API_KEY = ""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_PARAM = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY
}

NEWS_PARAM = {
    'q': COMPANY_NAME,
    'sortBy': 'popularity',
    'apikey': NEWS_API_KEY
}


respond = requests.get(STOCK_ENDPOINT, params=STOCK_PARAM)
respond.raise_for_status()
stock_data = respond.json()
close_values_list = []

stock_relevant_days_data = dict(itertools.islice(stock_data["Time Series (Daily)"].items(), 2))
for (key, value) in stock_relevant_days_data.items():
    close_values_list.append(value['4. close'])


respond = requests.get(NEWS_ENDPOINT, params=NEWS_PARAM)
respond.raise_for_status()
news_articles = respond.json()['articles']

three_relevant_news_articles = news_articles[:3]

print(three_relevant_news_articles)

# first_3_articles = dict(itertools.islice(news_articles.items(), 3))
# print(first_3_articles)










## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

