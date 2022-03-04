a=int(input())
c=int(input())

def f(n,k):
    for i in range(n, k+1):
        yield i*i

b=f(a,c)
for i in range(a, c+1):
    print(next(b))