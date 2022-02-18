
def solve(numheads, numlegs):
    rabbits=(4*numheads-numlegs)/2
    chickens=numheads-rabbits
    return chickens,rabbits
    
# a=int(input())
# b=int(input())
a=35
b=94

rabbits,chickens=solve(a,b)

print(rabbits, chickens)