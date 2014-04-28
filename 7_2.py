n=int(raw_input('Number: '))
flag=1
try:
    f=open('j.txt')
except IOError:
    print "No such file or directory: "

for line in open('j.txt'):
    if int(line)==n:
        print 'yes'
        flag=0

if flag:
    print 'no'
