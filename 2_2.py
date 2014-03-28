a=raw_input("Enter the codeed string: ")
result=''
i=1
while i < len(a):
    if a[i-1]=='@':
        result+=a[i+1]*int(a[i])
        i+=1
    else:
        result+=a[i-1]
    i+=1
print result
