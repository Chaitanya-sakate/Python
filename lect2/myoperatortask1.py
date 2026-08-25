#3 digit number addition
number=int(input('enter a 3 digit number'))
a=number%10
number=number//10
print(a)
b=number%10
number=number//10
print(b)
c=number%10
number=number//10
print(c)
result=a+b+c
print(result)
