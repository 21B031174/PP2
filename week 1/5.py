a=input()
list=a.split(" ")
a1=int(list[0])
a2=int(list[1])
if a1<500:
    if a2%2==0:
        for i in range(2,a1):
            if a1%i==0:
                print("Try next time!")
                break
            if i==a1-1:
                print("Good job!")
    else:
        print("Try next time!")
else:
    print("Try next time!")