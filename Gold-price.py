import requests

url = "https://raw.githubusercontent.com/iran-market/iran-market.github.io/main/data/popular.json"
data = requests.get(url).json()

for item in data["data"]:
    if item["symbol"] == "GOLD_18K_IRR":
        print("قیمت طلای ۱۸ عیار:", item["price"], "تومان")
