import re
email=input("enter email id:")
pattern="[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
res=re.fullmatch(pattern,email)
if res:
    print("valid email")
else:
    print("invalid email")