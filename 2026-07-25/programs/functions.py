#lambda 
x=4
result=lambda x:x*x
print(result(x))
#map
n=[1,2,3,4,5]
result=map(lambda x:x*x,n)
print(list(result))
#filter
n=[1,2,3,4,5]
result=filter(lambda x:x%2==0,n)
print(list(result))
#redunce
from functools import reduce
n=[1,2,3,4,5]
result=reduce(lambda a,b:a+b,n)
print(result)
