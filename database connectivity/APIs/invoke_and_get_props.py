import requests
import json
respone=requests.get('https://jsonplaceholder.typicode.com/users')
data=respone.json()
print(data)