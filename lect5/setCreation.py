#set creation
a=set()
print(a)
s={1,2,3,4}
print(s)
#it is not allowed 2d
#s={1,2,3{1,2}}
#print(s)
s={1,1,1,2} # 1d aloowed
print(s)
s={1,'hello',2,True}
print(s)
s=set([1,2,3])
print(s)
#can not contain mutable datatypes
#s={1,2,3,[1,2]}
#print(s)