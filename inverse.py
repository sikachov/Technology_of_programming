a=[5,4,3,2,1,9,10,3]
k=0
for i in xrange(0,len(a)):
    for j in xrange(i,len(a)):
        if a[i]>a[j]:
            k+=1
print k
