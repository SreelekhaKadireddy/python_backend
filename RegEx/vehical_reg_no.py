import re
vNo=input("enter vehical number:")
pattern="KA[012][0-9][A-Z]{2}\d{4}" #ex:KA02XY6352
res=re.fullmatch(pattern,vNo)
if res:
    print("valid vehical number")
else:
    print("not valid")