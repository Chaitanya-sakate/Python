#min number find
fnum=int(input('enter a number'))
snum=int(input('enter a number'))
tnum=int(input('enter a number'))
if fnum<snum and fnum<tnum:
    print('fnum is smallest',fnum)
elif snum<tnum:
    print('snum is smallest',snum)
elif fnum>snum and fnum>tnum:
        print('fnum is greater',fnum)
elif snum>tnum:
        print('snum is greater',snum)
        print('tnum is greater')
else:
    print('tnum is smallest',tnum)
print('tnum is greater',tnum)