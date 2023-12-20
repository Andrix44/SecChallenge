import requests

with open("contracts.txt", 'r') as f:
    lines = f.readlines()

for line in lines:
    r = requests.get(line.split('?')[0])
    if("cd22" in r.text):
        print(r.url)
        print(r.text)
        exit()