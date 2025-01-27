import math


class Student:
    def getString(self):
        self.name=(string(input()))
    def printString(self):
        print(self.name)

class Shape:
    def __init__(self):
        self.area=0
    def area(self):
        print(self.area);
class Square(Shape):
    def __init__(self,length):
        self.length=length
        self.area=self.length*self.length
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def computeArea(self):
        area=self.length*self.width
        self.area=area
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"{self.x},{self.y}")
    def move(self,x,y):
        self.x=x
        self.y=y
    def dist(a,b):
        d=math.sqrt((a.x-b.x)**2+(a.y-b.y)**2);
        print(d)

class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,x):
        self.balance+=x
    def withdraw(self,x):
        if (self.balance>=x):
            self.balance-=x
        else:
            print("Withdraw cannot be more than the balance")
def find_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors
list_l=[]
n=100
for i in range(n):
    list_l.append(i);
#rem=lambda x,l:l-(for i in range(x*2,n,x))
rem = list(filter(lambda x : len(find_divisors(x))==2, list_l))
print(rem)

# for i in range(2,n):
#     l=rem(i);
# print(l)