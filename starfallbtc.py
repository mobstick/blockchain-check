# Import the necessary libraries
import sys
import time
import requests

# Function to check the transaction details on the blockchain
def check_transaction(tx_id):
  # Make a request to the blockchain API to get the transaction details
  r = requests.get("https://blockchain.info/tx/" + tx_id)
  data = r.json()

  # Check the transaction status
  if data["status"] == "success":
    return True
  else:
    return False

# Prompt the user to enter a Bitcoin address and a transaction amount
bitcoin_address = input("Enter the Bitcoin address: ")
amount = input("Enter the transaction amount: ")

# Check to see if the user has made the transaction
transaction_made = check_transaction(tx_id)

# Print the result
if transaction_made:
  print("Transaction successful!")
else:
  print("Transaction failed. Please try again.")
