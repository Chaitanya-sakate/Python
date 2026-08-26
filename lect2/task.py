#sequence number print-1/1!,2/2!......n th number
n=int(input('enter n number'))
fact=1
result=0
for i in range(1,n+1):
    result=result+i/fact
    print(result)
