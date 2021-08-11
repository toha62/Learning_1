import requests

url = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open('input.txt') as inf:
    url1 = inf.read().strip()

r = requests.get(url1)
while r.text[0:2] != 'We':
    url1 = url + r.text
    r = requests.get(url1)
    #print(r.text[0:2])

with open('text.txt', 'w') as onf:
    onf.write(r.text)


#print(len(r.text.strip().splitlines()))