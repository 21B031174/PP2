a=int(input())
k=0
def f(n):
    
    for i in range(n):
        if i%3==0 or i%4==0:
            yield i
    
b=f(a)
for i in range(a):
    try:
        print(next(b),end=" ")
    except Exception as e:
        print(str(e),end='')
    