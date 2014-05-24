first=[1,2,3,4,5,6,7,8,9]
second=[2,10,4,-4,6,-7,8,9,10]
result=''
flag=1
for i in xrange(len(first)):
    if first[i]+second[i]<0:
        symbol=''
    else:
        symbol='+'
    if first[i]+second[i]==1:
        value=''
    elif first[i]+second[i]==-1:
        value='-'
    else:
        value=str(first[i]+second[i])
    if first[i]+second[i]==0:
        flag=0
    if flag==1:
        if i==0:
            result+=str(first[i]+second[i])
        elif i==1:
            result+=symbol+value+'x'
        else:
            result+=symbol+value+'x^'+str(i)
    flag=1
print result
