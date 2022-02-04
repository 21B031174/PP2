s=str(input())
a=0
b=0
def rec(c,sum,i):
    if i==len(c):
        return sum
    sum+=int(c[i])*pow(2,len(c)-i-1)
    return rec(c,sum,i+1)
    
print(rec(s,a,b))