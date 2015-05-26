str=raw_input("Enter a string:")
leng=len(str)-1

str_rev=''

for i in range(leng,-1,-1):
    str_rev+=str[i]
print str_rev
    
