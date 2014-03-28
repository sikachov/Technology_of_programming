a=raw_input("Enter the string: ")
k=1
symbol=''
result=''
for i in xrange(1,len(a)):
    if a[i-1]==a[i]:
        k+=1
    else:
        if k>3:
            result+='@'+str(k)+a[i-1]
        else:
            result+=a[i-1]
        k=1
if k>3:
    result+='@'+str(k)+a[i-1]
else:
    result+=a[i]
print result
