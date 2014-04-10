mas=[10,2,5,3,8,9,2,3,4,11]
raz=10
raz=10-1
def m(a,n,maxi=mas[raz]):
    if n==0:
        return maxi
    if a[n-1]>maxi:
        maxi=a[n-1]
    n-=1
    return m(a,n,maxi)
print m(mas,raz)
        
    
