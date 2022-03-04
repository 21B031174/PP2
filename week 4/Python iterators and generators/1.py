a=int(input())
def f(n):
    for i in range(n):
        yield i*i

b=f(a)
for i in range(a):
    print(next(b))