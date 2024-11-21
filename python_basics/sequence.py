print("-----------1. List---------")
list1=[12,4,0,5,99,34,12,23,'raju']
print(type(list1))
print(list1)


print("-----------2. Set----------")
set1={12,4,0,5,99,34,12,23,99,3,2,12,'raju','raju','mohan'}
print(type(set1))
print(set1)


print("-----------3. Tuple--------")
tuple1=(12,4,0,5,99,34,12,23,99,3,2,12)
print(type(tuple1))
print(tuple1)

print("-----------4. String-------")
str1="mohan"
print(type(str1))
str1="raju"
print(str1)

str2='r'
print(type(str2))
print(str2)


print("-----------5. Range--------")
range(10)
ran = range(10)
list2 = list( range(1,10))
print(list2)
print(type(ran))


print("----------6. Dictnory------")
d1 ={'mohan':'redmi','kalyan':'samsung','srnivas':'iphone'}
print(d1)
print(type(d1))
print(d1.values())
print(d1.keys())
print(d1['kalyan'])
print(d1.get('kalyan'))