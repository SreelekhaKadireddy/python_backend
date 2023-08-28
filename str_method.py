def re_str(s):
    for char in range(0,len(s)):
        if (s[char].is()==False):
            s.replace(s[char],"#")
    return s

s=input("enter a string")
res=re_str(s)
print(res)