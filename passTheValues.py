from numpy import *
def update(x):

    x=8
    print(id(x))
    print("x = ",x)

a=10
print(id(a))
update(a)
print("a = ",a)

print("------------------------------------------")

def update1(lst):

    lst[1]=25
    print(lst)
    print(id(lst))
    print("lst", lst)

lst = [10,20,30]
print(id(lst))
update1(lst)
print(lst) # list is mutable in python