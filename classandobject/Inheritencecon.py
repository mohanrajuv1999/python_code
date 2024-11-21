
class A:
    def feature1(self):
        print('Fetures1')

    def feature2(self):
        print('fetures2')

class B:
    def feture3(self):
        print('fetures3')

    def fetures4(self):
        print('fetures4')

class C(A,B):
    def feture5(self):
        print('fetures5')

    def feture6(self):
        print('fetures6')


c1 = C()
c1.feature1()
c1.feture6()