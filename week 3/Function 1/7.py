def has(a):
    if 3 in a:
        if a[a.index(3)+1]==3:
            return True
        else:
            return False
    else:
        return False
q=list(map(int, input().split()))
a=has(q)
if a==True:
    print("True")
else:
    print("False")