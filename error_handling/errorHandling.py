fp=open("data.json",'r')
try:
    r=10/0
    res=10*a

except SyntaxError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)
    fp.close()
