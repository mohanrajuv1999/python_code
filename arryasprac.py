from array import *

arr = array('i',[])
n=int(input("Enter the size of the aray: "))

for i in range(n):
    arr.append(int(input("Enter the elements: ")))

print(arr)


f = int(input("Enter the number: "))
for e in arr:
    if e==f:
        print(arr.index(f))
        break
    else:
        print("element not there")
