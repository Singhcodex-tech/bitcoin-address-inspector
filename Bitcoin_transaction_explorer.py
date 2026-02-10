import requests

# Function to fetch transaction data
def get_transaction(txid):
    
    url = f"https://blockstream.info/api/tx/{txid}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print("❌ Transaction not found")
        return None
    
    return response.json()


# Function to analyze transaction
def analyze_transaction(tx_data):
    
    print("\n📊 Transaction Analysis")
    print("=" * 40)
    
    # Transaction ID
    print(f"Transaction ID: {tx_data['txid']}")
    
    # Confirmation Status
    confirmed = tx_data['status']['confirmed']
    print(f"Confirmed: {confirmed}")
    
    # -------- Inputs (Senders) --------
    print("\n💸 Senders:")
    total_input = 0
    
    for vin in tx_data['vin']:
        if 'prevout' in vin:
            address = vin['prevout'].get('scriptpubkey_address', "Unknown")
            value = vin['prevout']['value'] / 100000000   # satoshi → BTC
            total_input += value
            
            print(f"Address: {address}")
            print(f"Amount Sent: {value} BTC\n")
    
    # -------- Outputs (Receivers) --------
    print("\n🎯 Receivers:")
    total_output = 0
    
    for vout in tx_data['vout']:
        address = vout.get('scriptpubkey_address', "Unknown")
        value = vout['value'] / 100000000
        total_output += value
        
        print(f"Address: {address}")
        print(f"Amount Received: {value} BTC\n")
    
    # -------- Fee Calculation --------
    fee = total_input - total_output
    
    print("💰 Summary")
    print("-" * 40)
    print(f"Total Input: {total_input} BTC")
    print(f"Total Output: {total_output} BTC")
    print(f"Transaction Fee: {fee} BTC")


# -------- MAIN PROGRAM --------
if __name__ == "__main__":
    
    txid = input("Enter Bitcoin Transaction ID: ")
    
    tx_data = get_transaction(txid)
    
    if tx_data:
        analyze_transaction(tx_data)
