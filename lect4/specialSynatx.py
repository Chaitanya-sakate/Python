#special syantax
a,b,c=(1,2,3)
print(a,b,c)

#extra values not needed
a,b,*others=(1,2,3,4,5)
print(a,b)
print(others)

#zip
a=(1,2,3)
b=(4,5,6)
print(tuple(zip(a,b)))