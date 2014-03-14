num=input('Number: ')
sys=input('System: ')
number=[]
while num>0:
    number.append(num%sys)
    num/=sys
print number
a=len(number)
k=0
flag=False
if a%2==0:
    count=a/2+1
    flag=True
else:
    count=a/2+2
for i in xrange(1,count):
    if number[i-1]!=number[i*(-1)]:
        print "Not polindrom"
        break
    else:
        k+=1
if flag:
    if k==(a/2):
        print 'Polindrom'
else:
    if k==(a/2)+1:
        print 'Polindrom'
