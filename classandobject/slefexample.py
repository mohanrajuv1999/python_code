
class Laptop:
    def Dell(self, name,age):
        self.name = name
        self.age = age


    def Hp(self):
        print(self.name)
        print(self.age)


l1 = Laptop()
l1.Dell('raju',28)
l1.Hp()