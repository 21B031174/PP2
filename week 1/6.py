a=int(input())
list=[]
for i in range(0,a):
    b=int(input())
    if b<=10:
        list.append("Go to work!")
    elif b>10 and b<=25:
        list.append("You are weak")
    elif b>25 and b<=45:
        list.append("Okay, fine")
    else:
        list.append("Burn! Burn! Burn Young!")
for i in range(0,a):
    print(list[i])