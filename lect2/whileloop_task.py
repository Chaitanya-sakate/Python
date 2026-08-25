#guessing game
import random
jackpot=random.randint(1,100)
guess=int(input('guess karo'))
count=1
while guess!=jackpot:
    if guess<jackpot:
        print('wrong,enter higher')
    else:
        print('wrong,enter lower')
    guess=int(input('guess karo'))
    count+=1
else:
    print('correct guess')
    print('attempts',count)





