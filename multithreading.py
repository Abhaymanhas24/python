from threading import Thread
from time import sleep


class Sample(Thread):
    def m1(self):
        print("m1")

    def run(self):
        for i in range(1, 5):
            print(i)
            sleep(1)
        self.m1()


class Demo(Thread):
    def run(self):
        for i in range(6, 11):
            print(i)
            sleep(1)


obj1 = Sample()
obj2 = Demo()
obj1.start()
obj2.start()
obj1.join()
obj2.join()
print("i am at the end")
