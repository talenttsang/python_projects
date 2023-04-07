import requests

r = requests.get('https://www.op.gg/')

print(r.headers)