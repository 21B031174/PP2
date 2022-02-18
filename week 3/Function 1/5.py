from itertools import permutations

a=list(map(int, input().split()))

n=list(permutations(a))

for i in n:
    print(i)

