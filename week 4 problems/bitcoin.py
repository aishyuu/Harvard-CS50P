"""
Implement a program that
Expects the user to specify the number of bitcoin that they would like to buy
    This is given from the command line (sys library)
    If the argument can't be converted to float, sys.exit

Query the API for CoinDesk Bitcoin Price Index
    https://api.coindesk.com/v1/bpi/currentprice.json
Among the nested keys is the current price of bitcoin as a float

Outputs the current cost of n Bitcoins in USD to four decimal places
    Requests library
Use "," as a thousands separator
"""

import sys
import requests

try:
    bitcoin_want = float(sys.argv[1])
except IndexError:
    print("No command line argument")
    sys.exit()
except ValueError:
    print("Command line argument is not a number")
    sys.exit()
    
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin_json = response.json()
except requests.RequestException:
    print("Error gathering API")
    sys.exit()

bitcoin_price = float(bitcoin_json["bpi"]["USD"]["rate_float"])
amount = bitcoin_want * bitcoin_price
print(f"${amount:,.4f}")