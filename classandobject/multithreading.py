from threading import *
from time import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


h1 = Hello()
h2 = Hi()
h1.start()
h2.start()

h1.join()
h2.join()

print("Bye")
