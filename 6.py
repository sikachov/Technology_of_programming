filename=raw_input("Enter the name of file: ")
position=int(raw_input("Position: "))
finish=int(raw_input("Finish: "))
f=open(filename)
a=f.readline()
mas=[]
result=''
for i in xrange(position,finish):
    mas.append(hex(ord(a[i])))
    
for i in mas:
    b=i.split("0x")
    result+=b[1]+" "

print result
