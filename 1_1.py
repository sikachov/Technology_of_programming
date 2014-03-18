a=raw_input("Enter: ")
a=a.split("+")
print a
b=[]
for i in a:
    b.append(int(i.split("-")))
for i in xrange(len(b)):
    res=sum(i)
    print i
