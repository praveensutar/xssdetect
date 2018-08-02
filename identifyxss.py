import requests, re


### Read payload file for xss attack testing
fname = "payloads.txt"
with open(fname) as f:
    content = f.readlines()
# Remove  `\n`
pattern = '/^((http|https):\/\/)/'
payloads = [x.strip() for x in content]
url = raw_input("URL: ")

test = re.findall('http[s]?://', url)
#print(test)
if test:
    print("### Protocol present")
else:
    print('### Adding protocol in URL ')
    url = 'http://'+url
    print("#### Input URL=  %s" % (url))
vuln = []
try:
    for payload in payloads:
        payload = payload
        new_url = url+'/'
        xss_url = new_url+payload
        r = requests.get(xss_url, verify=False)
        if payload.lower() in r.text.lower():
            print("####################################################################################")
            print("########## Vulnerable Payload: " + xss_url)
            print("####################################################################################")
            if(payload not in vuln):
                vuln.append(payload)
        else:
            print("URL Not vulnerable!!")
except:
    print("#### Exceptions in URL....")
