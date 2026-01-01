import requests
import sys
import json

API_KEY='7d9a70692a40e9e14a6c5d1e59c90012aff11b51b348d8dc32e4698599bd1a7b'
url=f'https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}'
key='priceUsd'

if len(sys.argv)==1:
    sys.exit('Missing command-line argument')

try:
    n=float(sys.argv[1])
except Exception:
    sys.exit('Command-line argument is not a number')


resp=requests.get(url).json()
price=float(resp['data'][key])
total_price=n*price
print(f'${total_price:,.4f}')
