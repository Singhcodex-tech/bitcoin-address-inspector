import requests

def fetch_address_data(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code != 200:
            print("Invalid address or API error")
            return None
        return response.json()
    except requests.exceptions.RequestException:
        print("Network error")
        return None

def check_activity(data):
    tx_count = data.get("n_tx", 0)
    return "Active" if tx_count > 0 else "Inactive"

def get_balance(data):
    satoshis = data.get("final_balance", 0)
    return satoshis / 1e8

if __name__ == "__main__":
    api_url = input("Enter blockchain API URL for the address: ").strip()
    data = fetch_address_data(api_url)

    if data:
        print(f"Account status: {check_activity(data)}")
        print(f"Final balance: {get_balance(data)} BTC")
