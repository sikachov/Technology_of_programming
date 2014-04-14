count=0
for i in xrange(1000):
    if ((2**i)-i)%7==0:
        count+=1

print count
