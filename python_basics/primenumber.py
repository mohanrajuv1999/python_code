for i in range(1,101):
    if(i%2==0 and i%i==0):
        pass
    else:
        print(i, end=",")

print("--------------------------")
x = int(input("enter the number: "))

if x%2 == 0 and x%x == 0:
    print(str(x)+" is not prime number")
else:
    print(str(x)+" is a prime number")
