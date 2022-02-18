
def histogram(lis):
    
    p=[]
    for i in lis:
        a=""
        for i in range(i):
            a+="*"
        p.append(a)
    return p


a=list(map(int, input().split()))
b=histogram(a)
for i in range(len(a)):
    print(b[i])
