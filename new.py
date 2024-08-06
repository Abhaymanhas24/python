# # import function
# from function import add
# add(1,2)

# class Sample:
#     name='Python'
#     def n(self):
#         print("lllli")
    
   

# class Demo(Sample):
#     def n2(self):
#         print('hi')

# obj1=Demo()
# obj1.n()
# obj1.n2()

class Iphone13:
    def camera(self):
        print("15")

class Iphone14(Iphone13):
    def camera(self):
        print("20")

class Iphone15(Iphone14):
    def camera(self):
        print("30")
        super().camera()
    def display(self):
        print("dynamic")
    
obj15=Iphone15()
obj15.camera()
obj15.display()