import datetime as dt
import pandas as pd

data = pd.read_csv("birthdays.csv")
dates = {(row['day'], row['month']): row['name'] for (index, row) in data.iterrows()} ###########

today_tuple = (dt.datetime.now().day, dt.datetime.now().month)

if today_tuple in dates:
    print(dates[today_tuple])
