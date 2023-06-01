import os
from datetime import datetime, timedelta

import requests

STOCK = "TSLA"
COMPANY_NAME = "tesla"
ALPHAVANTAGE_API_KEY = ''
NEWS_API = ''

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    'symbol': STOCK,
    'apikey': ALPHAVANTAGE_API_KEY,
    'function': 'TIME_SERIES_DAILY_ADJUSTED'
}

response = requests.get('https://www.alphavantage.co/query', params=parameters)
stock_data = response.json()
last_day = stock_data['Meta Data']['3. Last Refreshed'].split('-')
formatted_last_day = datetime(year=int(last_day[0]), month=int(last_day[1]), day=int(last_day[2])).date()
previous_day = formatted_last_day - timedelta(days=1)

last_day_value = float(stock_data['Time Series (Daily)'][str(formatted_last_day)]['4. close'])
previous_day_value = float(stock_data['Time Series (Daily)'][str(previous_day)]['4. close'])


def percentage(today_val, yesterday_val):
    return 100 - (yesterday_val * 100 / today_val)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

parameters = {
    'q': COMPANY_NAME,
    'from': str(formatted_last_day),
    'sortBy': 'publishedAt',
    'apiKey': NEWS_API
}

response = requests.get('https://newsapi.org/v2/everything', params=parameters)
print('news', response.json())
news_data = response.json()['articles'][:3]
print(len(news_data))
print(news_data)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


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

