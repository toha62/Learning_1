import requests

with open('input.txt') as inf:
    url = inf.read().strip()

print(url)

r = requests.get(url)

print(len(r.text.strip().splitlines()))