# def m1(a,b):
#     return a * b


def m1(a1):
    
    new_List =[]
    for i in a1:
       i =i*2
       new_List.append(i)
    return new_List
    
a1 =[5,3,7,3,8]
print(m1(a1))
# map applies logic to each and every element
b1= list(map(lambda x:x*2,a1))
print(b1)

def m3():
    a3=["1","2","3"]
    for i in range(len(a3)):
        a3[i]=int(a3[i])
    return a3
print(m3())
a3=["1","2","3"]
l=list(map(int,a3))
print(l)

# Reduce -- takes the 2 parameters and applies the result with next value

x1=[3,6,3,7]
from functools import reduce
out= reduce(lambda a,b:a+b,x1)
print (out)

# from itertools import accumulate
# x1 = [3, 6, 3, 7]
# running_totals = list(accumulate(x1))
# print(running_totals)

# filter
a1=[1,2,3,4,5,6,7]
oooo= list(filter(lambda x: x%2==0,a1))
print(oooo)

empno=[101,102,103,104]
ename=["abc","bcd","cde","def"]
emp=dict(zip(empno,ename))
print(filter(lambda x:x >=102,emp.keys()))