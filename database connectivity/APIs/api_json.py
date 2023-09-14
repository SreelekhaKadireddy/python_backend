import requests
import json
res=requests.get('https://jsonplaceholder.typicode.com/users')
users_list=res.json() #data in the form of list
"""
fp=open('users.json','w')
json.dump(users_list,fp)
fp.close()
"""
# write only required fields in json file(id,name,email)
fp=open('users1.json','w')
for user in users_list:
    json.dump(user['name'],fp)
    
fp.close()
