x=1;
while(x!=0):
    a = int(input('Enter the number= '))
    b= int(input('Enter the divider= '))
    try:
        c=a/b
        print(c)
    except ZeroDivisionError as e:
        print("The number is Zero",e)

    except Exception as e:
        print("something went wrong")

    finally:
        print("closed")

