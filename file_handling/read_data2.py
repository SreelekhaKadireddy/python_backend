import csv
f=open('one.csv','r')
cp=csv.reader(f)
print(cp)
print(type(cp))
data=list(cp)
for line in list(data):
    print(line)