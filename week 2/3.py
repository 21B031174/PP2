a=int(input())
k=1
l=0
for i in range(a):
    for j in range(a):
        if i==0:
            print(j, end=' ')
        elif j==0:
            print(k, end=' ')
            k+=1
        elif i==j:
            print(i*j, end=' ')
        else:
            print(l, end=' ')
    print()
    