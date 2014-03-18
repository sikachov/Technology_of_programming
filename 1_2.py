a=raw_input('Enter: ')
flag=False
countOpen=0
countClose=0
for i in a:
    if i=='(':
        flag=True
        countOpen+=1
    elif flag:
        if i==")":
            countClose+=1

if countClose==countOpen:
    print "Ok"
else:
    print "Error!"
