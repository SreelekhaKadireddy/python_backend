import json
f=open('one.json')
python_dict=json.load(f)
print(python_dict)
for item in python_dict.items():
    print(item)