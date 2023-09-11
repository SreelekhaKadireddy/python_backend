
fp=open(fileName,'r')
data=fp.read()
print(data)
try:
    fileName=input('enter file name:')
except (FileNotFoundError,IndexError,ZeroDivisionError):
    print("except block")
    fp=open(fileName,'r')
    data=fp.read()
    print(data)
finally:
    fp.close()
    print("finally block")