import random
t=int(input('How many times you want to try: '))
randomNumber = random.randrange(1,10)
for i in range(t):
    n =int(input())
    if n==randomNumber:
        print('You are winner!!')
    else:
        print('You are loser....')

