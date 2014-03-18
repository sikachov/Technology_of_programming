word=raw_input("Enter the word: ")
string=''
original=[]
cnt=[]
for i in word:
    if i not in original:
        original.append(i)
for i in original:
    cnt.append(word.count(i))
print original
print cnt
for i in xrange(len(cnt)):
    a=max(cnt)
    for i in xrange(a):
        string+=str(original[cnt.index(a)])
    cnt.remove(a)
print string

