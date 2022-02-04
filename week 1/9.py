a=int(input())
list=[]
for i in range(0,a):
    s=str(input())
    if "@gmail.com" in s:
        list.append(s[:-10])
for i in range(0, len(list)):
    print(list[i])