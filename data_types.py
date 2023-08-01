#python data types
#int

a=10
b=0b1101
c=0o147
d=0xacd3
print(a)
print(b)
print(c)
print(d)
print(int(0x2ff))
print(oct(13))
print(bin(134))
print(hex(10))

#float

a=15
print(float(a))
print(float("10"))
print(float(False))

#list
l=[10,10,30,255]
for a in l:
    print(a)
#list is mutable,duplicate values are allowed
#bytes
b=bytes(l)
print(b)
print(b[1])
#bytearray
ba=bytearray(l)
print(ba)
print(ba[2])
#'bytearray' is mutable whereas 'bytes' is immutable 