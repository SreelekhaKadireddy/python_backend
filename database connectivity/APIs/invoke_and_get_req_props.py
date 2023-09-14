import requests
import json
respone=requests.get('https://jsonplaceholder.typicode.com/users')
data=respone.json()
for prop in data:
    print(prop['id'],":",prop['name'])