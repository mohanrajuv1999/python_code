
def greet():
    print('Hello')
greet()


def add(x,y):
    z=x+y
    return z

ans= add(2,3)
print(ans)

add(3,5)

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result1, result2 =add_sub(7,8)
print(result1,result2)