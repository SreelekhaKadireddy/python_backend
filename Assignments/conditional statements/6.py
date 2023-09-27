#digit to words
num=int(input())
dict={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
for temp in dict:
    if num==temp:
        print(dict[temp])