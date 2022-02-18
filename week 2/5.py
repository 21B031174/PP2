a=input().split()
if len(a)>1:
    x,y=a[0],a[1]
else:
    x=a[0]
    y=int(input())
sum=0
for i in range(int(x)):
    sum^=int(y)+2*i
print(sum)