import requests
from twilio.rest import Client
import datetime
STOCK = "TSLA" # any 4 letter stock
COMPANY_NAME = "Tesla Inc" # any company stock you pick
now = datetime.datetime.now()
today = now.day


# Get stock closing number for yesterday and day before
url = 'https://www.alphavantage.co/query'
paramater = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "The key you get when you sign up",
}
response = requests.get(url, params=paramater)
response.status_code
data = response.json()

day_b4_float = float(data["Time Series (Daily)"]["The day before date in yyyy-mm-dd format"]["4. close"])
yesterday_float = float(data["Time Series (Daily)"]["Yesterday date in yyyy-mm-dd format"]["4. close"])

yesterday = int(yesterday_float)
day_b4 = int(day_b4_float)

if yesterday > day_b4:
    stock_increase = yesterday - day_b4
    decimal_num = stock_increase / day_b4
    total_percent = round(decimal_num, 3) * 100
    my_answer = f"🔺{int(total_percent)}%"
else:
    stock_increase = day_b4 - yesterday
    decimal_num = stock_increase / day_b4
    total_percent = round(decimal_num, 3) * 100
    my_answer = f"🔻{int(total_percent)}%"


# Get the news for the company to see the insights on them
new_paramater = {
    "q": COMPANY_NAME,
    "from": f"2022-05-{today}",
    "apiKey": "The key you get when you sign up",
}
article = requests.get("https://newsapi.org/v2/everything", new_paramater)
article.status_code
new_data = article.json()

headline = new_data["articles"][0]["title"]
description = new_data["articles"][0]["description"]


# Send a text with the stock info to your cell phone
account_sid = "The account_sid you get when you sign up"
auth_token = "The auth_token you get when you sign up"
client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                    body=f"your stock code ex:TSLA: {my_answer}\nHeadline: {headline}\nBrief: {description}",
                    from_="The phone number you get when you sign up",
                    to="To your number or any number you put in"
                )
