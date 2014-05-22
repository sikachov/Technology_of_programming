a=[1,2,3]
res=[]
res.append(a)
for i in xrange(1,len(a)+1):
    for j in xrange(i,len(a)+1):
        if i==j:
            res.append([i])
        else:
            res.append([i,j])
print res
