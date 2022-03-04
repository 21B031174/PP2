a=int(input())
def f(n):
    for i in range(n+1):
        yield n-i
    
b=f(a)
for i in range(a+1):
    print(next(b),end=" ")
    
    