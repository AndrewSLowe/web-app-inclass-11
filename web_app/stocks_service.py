
# web_app/stocks_service.py

import requests
import json

# With urls, look for api parameters to change what data I get. Also, this api uses authentification by url `apikey=abc123`
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=abc123" 
print(request_url)

response = requests.get(request_url)
print(type(response)) #> <class 'requests.models.Response'>
print(response.status_code) #> 200
print(type(response.text)) #> <class 'str'>

data = json.loads(response.text)   # Turns the response which is a json-like-string to a puthon dictionary
print(type(data)) #> <class 'dict'>

latest_close = data["Time Series (Daily)"]["2020-02-25"]["4. close"]
print("LATEST CLOSING PRICE:", latest_close)

#breakpoint()
