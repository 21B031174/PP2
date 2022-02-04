s=input()
ch=input()
list=[]
for i in range(0,len(s)):
    if s[i]==ch:
        list.append(i)
if len(list)==0:
    print("")
elif len(list)==1:
    print(list[0])
else:
    print(str(list[0])+" "+str(list[-1]))