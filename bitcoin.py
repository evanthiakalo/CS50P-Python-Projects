import sys
import requests
if len(sys.argv)!= 2:
    sys.exit("Missing command-line argument")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
API_KEY = "e12a7fe17302e7f0f553c90e6605de317e59df8dc5adaa754b8d72c429e3adf3"
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"
try:
    response = requests.get(url)
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Request failed")
total = n* price
print(f"${total:,.4f}")
