num=input('Number: ')
sys=input('System: ')
arr=[]
while num>0:
    arr.append(num%sys)
    num/=sys
print arr
k=1
for i in xrange(0,len(arr)):
    for j in xrange(i+1,len(arr)):
        if arr[i]==arr[j]:
            k+=1
            if k==2:
                print "Yes"
                break
    if k==2:
        break
if k!=2:
    print "No"
