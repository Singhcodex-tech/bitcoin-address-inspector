#Program to fetch the balance of Bitcoin 
import requests
url =input("Enter an address to check your bitcoin balance : ").strip()
response = requests.get(url)
if(response.status_code==200):
    print(response.status_code)
    data=response.json()
    balance_satoshish = data.get("final_balance",0)
    final_balance = balance_satoshish/1e8
    print(balance_satoshish)
    print(final_balance)
else:
    print("Incorrect address")

