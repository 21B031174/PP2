from random import randint as rand


print("Hello! What is your name?")
name=input()
print()
print(f'Well, {name}, I am thinking of a number between 1 and 20.')    

num=rand(1,20)
b=0
while True:
    print("Take a guess.")
    a=int(input())
    b+=1
    print()
    if num==a:
        print(f'Good job, {name}! You guessed my number in {b} guesses!')
        break
    else:
        if a>num:
            print('Your guess is too high.')
        else:
            print('Your guess is too low.')

