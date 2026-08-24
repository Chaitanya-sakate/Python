#login website
email = input('enter email :')
password = input('enter password :')
if email =='chaitu@gmail.com' and password =='1234':
    print('welcome')
elif email =='chaitu@gmail.com' and password =='123':
    print('incorrect password')
    password=input('enter password again') 
    if password == '1234':
        print('shabass! you enter correct password')
    else:
        print('beta tumse na ho payega')
else:
    print('not correct') 
       


