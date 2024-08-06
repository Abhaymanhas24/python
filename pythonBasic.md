# Basic

## Variables

- memory holder -- singular Value

# oops

## class

- its a blueprint
- a collection of data (variables) and methods (functions)

## Object

- object is used call the class or store the address location of class
- object is like declaring a variable to class
- `self` is used to refers to the instance of the class you are in and access the obj instance variable defined

```py
  class Sample:
    name='Python'
    def n(self):
        print("hi")

obj1=Sample()
obj1.n()
print(obj1.name)
```

## Inhreitance

- when parent class can be called by sub class or child class

### single

```py
   class Sample:
    name='Python'
    def n(self):
        print("lllli")



class Demo(Sample):
    def n2(self):
        print('hi')

obj1=Demo()
obj1.n()
obj1.n2()

```

### Multi level

```py

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
```

### Hierarchical

- from one parent class to many child or subclass

```py
   class teacher:
    def english(self):
        print("English Language")
class student1(teacher):
    def language(self):
        print("english teacher should")
class student2(teacher):
    def language(self):
        print("english teacher should")

obj1=student1()
obj2=student2()

obj1.english()
obj1.language()
```

### Hybrid

### Multiple

- in this type of herarchical there are many parent to one child or subclass

```py
class Father:
   def gender(self):
       print("male")
class Mother:
   def gender(self):
       print("Female")
class child(Father,Mother):
   def gender(self):
       print("male")

obj1=child()
obj1.gender()
```

## Overriding

- allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes
- like the super used in inheritance to feach data from grandfather class

## Constructer

- it automatically call the function when we call the object as the first priority

```py
  def __init__(self)
      print("constructer is made")
```

## Abstraction

- used to hide irrelevant details from the user and show the details that are relevant to the users

```py
from abc import ABC,abstractmethod

class Account:
    def saving(self):
        print("zero balance account")

class Cards(ABC):
    @abstractmethod
    def cashback(self):
        pass
    def easypay(self):
        pass

class Cards1(Cards):
    def cashback(self):
        print("cashback cerid card")

obj1= Cards1()
```

# ERROR AND EXCEPTION HANDLING

- error handling is used with try and except in which we give the logic in try statement and if it doesnot work we write the except statement with the exception type like

  - IndexError
  - ZeroDivisionError
  - if we gi

  ## Iterators in Python

  ## Multithreading

  - it is used whe se want to run the two class simultaneously
  - `.join` is used to execute the full function first

```py
from threading import Thread
from time import sleep
class Sample(Thread):
def m1(self):
    print("m1")
def run(self):
    for i in range(1,5):
        print(i)
        sleep(1)
        self.m1()

class Demo(Thread):
def run(self):
    for i in range(6,11):
        print(i)
        sleep(1)

obj1 =Sample()
obj2=Demo()
obj1.start()
obj2.start()
obj1.join()
obj2.join()
print("i am at the end")
```

## File Handling

### Write

```py
f1= open("one.text","w")
f1.write("welcome to File Handling \n")
f1.write("File with write operation \n")
```

### Read

- it is used to read or print the data available in the file isf you want to print the whole data we use `.read()` but if we want one line at time we can use `.readline()`

```py
f1=open("one.text","r")
print(f1.read())
f1.close()
f2= open("one.text","r")
for i in range(1,4):
    print(f2.readlines(i))
```

### Append

- to add data in file without overwritting the file

```py
f1= open("one.text","a")
f1.write("wlecome \n")
```
