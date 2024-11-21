x=[2,9,'mohan',34,90,43]

for i in x:
    print(i)

y="mohanraju"

for i in y:
    print(i, end="-" "\n")
print()
print("-----------------------------")
for i in range(1,11):
    print(i)
print("--------------------")
# printing numbers in reverse order
for i in range(21,10,-1):
    print(i)

print("-------------------------------")
for i in range(1,101):
    print(i)
    continue

    # if i%3==0 or i%5==0:
    #     pass
    # else:
    #     print(i)

b=4
for i in range(4):
    for j in range(b):
        print("#",end="")
    print()
    b=b-1

print("---------------------------------")

nums=[4,8,9,35,88,99]
for i in nums:
    if i%5==0:
        print(i)
        break
else:
    print("Not found")