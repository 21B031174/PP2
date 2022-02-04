a=int(input())
s=input()
if s=="k":
    d=int(input())
    c=round(float(a/1024),d)
    print(c)
else:
    print(a*1024)