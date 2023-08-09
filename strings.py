
s=input()
#multiline strings
a='''This is a multi
line
string '''
print(s)
print(a)
print(s[1])#accessing char from a str
string="hello"
for ch in string:
    print(ch)
#check the presence of particular char in given str
print("e" in string)
print("z" not in string)

#slicing
x="hello, good morning"
print(x[:])
print(x[3:])
print(x[:5])
print(x[-2:])
print(x[:-3])
print(x[-8:-2])
s=s.upper()
a=a.lower()
print(s)
print(a)
#strip()
temp=" Hello "
print(temp.strip())
#replace()
print(temp.replace("H","J"))
#split()-returns list with elements as substrings between seperators
print(x.split(","))
#concatination
print(a+s)
print(string+" "+temp)
#string formaters
text="I'm sreelekha {}" #place holder
print(text.format("21"))
#escape char
ex="The person is from \"Italy\" "
print(ex)
