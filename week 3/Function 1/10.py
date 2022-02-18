def fun(s):
    list=[]
    for i in s:
        if i not in list:
            list.append(i)
    return list
a=input().split()

print(fun(a))
