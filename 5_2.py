n=int(raw_input("Enter: "))
f=1
s=1
fib=1
flag=0
for i in xrange(1,n):
   f=s
   s=fib
   fib=f+s
   if fib==n:
       flag=1
if n==1:
    flag=1
if flag:
    print "fib"
else:
    print "ne fib"
