pos = 0


def search(list, n):

    i = 0
    while i < len(list1):
        if list1[i] == n:
            globals()['pos'] = i
            return True
        i=i+1
    return False


list1 = [4, 8, 6, 9, 2, 1]
n = 9


if search(list1, n):
    print("Found", pos)

else:
    print("Not found")

search(list1, n)