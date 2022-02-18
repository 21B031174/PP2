
def ars(x):
    return int(x)

a=input()
s=input()
list=s.split(" ")

list.sort(key = ars)
print(int(list[-1])*int(list[-2]))
