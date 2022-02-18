a=int(input())
if a%2==1:
    for i in range(a):
        for j in range(a):
            if i+j<a-1:
                print(".", end='')
            else:
                print("#", end='')
        print()
else:
    for i in range(a):
        for j in range(a):
            if i>=j:
                print("#", end='')
            else:
                print(".", end='')
        print()
