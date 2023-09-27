import re
f=open('data.txt','r')
input=f.read()
print(input)
emails = re.findall(r'[\w\.-]+@[\w\.-]+', input)
print(emails)
f.close()