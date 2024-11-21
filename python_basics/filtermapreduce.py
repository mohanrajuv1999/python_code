from functools import reduce
num1=[2,8,6,4,7,9,11,15]
even1 = list(filter(lambda n:n%2==0,num1))
print(even1)

mul = list(map(lambda n:n*2,num1))
print(mul)

sum = reduce(lambda a,b:a+b,num1)
print("sum = ",sum)