#atm software
print("""if you want to pin readable, enter 1
if you want withdraw , enter 2 
if you want pin change,enter 3
if you want exit , enter 4""")
number=int(input('enter a number'))
if number==1:
    print('pin readable :abc')
elif number==2:
    print('withdraw money')
elif number ==3:
    print('pin change') 
elif number==4:
    print('exit')
else:
    print('you are wrong enter number')