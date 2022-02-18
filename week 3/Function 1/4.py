
def filter_prime(s):
    list=[]
    
    for i in s:
        ok=True
        for j in range(2,i):
            if i%j==0:
                ok=False
            
        if i==1 or i==0:
                ok=False
        if ok==True:
            list.append(i)
    return list
    
a=list(map(int, input().split()))

b=filter_prime(a)

print(b)
