import requests
import sys
lines = []

with open(sys.argv[1], 'r') as wordlist:
    lines = wordlist.readlines()

for i in lines:
    response = requests.get(f'http://172.25.0.20?guess={i}')
    currentPageText = response.text
    if "wrong!" not in currentPageText:
        print(response.text)
