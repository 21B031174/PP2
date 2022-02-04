s=str(input())
list=s.split()
string=""
for i in range(0,len(list)):
    if len(list[i])>2:
        string=string+(list[i]+" ")
print(string)