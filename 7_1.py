def elem(m,mas,mas1):
    for i in m:
        if i in mas:
            if i in mas1:
                return i



a=[1,2,3,4,5,6,7]
b=[-2,0,2,7,8,9,10]
c=[2,6,9]

if len(a)<len(b) and len(a)<len(c):
    print elem(a,b,c)
elif len(b)<len(a) and len(b)<len(c):
    print elem(b,a,c)
elif len(c)<len(b) and len(c)<len(a):
    print elem(c,b,a)
else:
    print elem(a,b,c)
