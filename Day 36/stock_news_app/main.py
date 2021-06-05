import requests
import datetime
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = os.environ.get('TWI_ACC_SID')
auth_token = os.environ.get('TWI_AUT_TOK')

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': os.environ.get('STK_API_KEY')
    }

news_params = {
    'qInTitle': COMPANY_NAME,
    'apiKey': os.environ.get('NWS_API_KEY')
    }

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

latest_date = str(datetime.date.today() - datetime.timedelta(days=1))
prev_date = str(datetime.date.today() - datetime.timedelta(days=2))
dates = [latest_date, prev_date]
stock_response = requests.get(url='https://www.alphavantage.co/query', params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()['Time Series (Daily)']
actuals = [float(value['4. close']) for key, value in stock_data.items() if key in dates]
diff = round((actuals[0] - actuals[1]) / actuals[1] * 100)
diff_percent_symbol = f"🔺{diff}%" if diff > 0 else f"🔻{diff}%"
if abs(diff) > 5:

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    news_response = requests.get(url='https://newsapi.org/v2/everything', params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()['articles'][:3]
    for news in news_data:
        content =f"{STOCK}: {diff_percent_symbol}\nHeadline: {news['title']}.\nBrief: {news['description']}"

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=content,
            from_=os.environ.get('TWI_PHN_NUM'),
            to=os.environ.get('ABI_PHN_NUM')
            )
        print(message.status)


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

