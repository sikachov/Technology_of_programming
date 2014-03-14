a=int(raw_input("A: "))
b=int(raw_input("B: "))
c=int(raw_input("C: "))

if ((a+b)>c)and((c+b)>a)and((a+c)>b):
    print "Yes"
    if (a**2+b**2==c**2)or(b**2+c**2==a**2)or(a**2+c**2==b**2):
        print "90"
    else:
        print "No 90"
else:
    print "No"

