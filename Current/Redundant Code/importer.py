import requests

res = requests.get("https://test-insight.bitpay.com/api/block/00000000a967199a2fad0877433c93df785a8d8ce062e5f9b451cd1397bdbf62")

print (res.json()["height"])