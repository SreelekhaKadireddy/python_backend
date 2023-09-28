import re
mobile=input("enter a mobile number:")
res=re.fullmatch("[6-9]\d{9}",mobile)
if res:
    print("valid indian mobile number")
else:
    print("not a valid indian moile number")