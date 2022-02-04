a=int(input())
s=input()
if s=="k":
    z=int(input())
    r=round(float(a/1024), int(z))
    print(r)
else:
    print(a*1024)