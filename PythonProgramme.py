#find square root of number
from datetime import  date


class Person():
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob

    def age(self):
        days=date.today().year-self.dob.year
        print('The current age of', self.name , 'is', days)
ajaydob=date(1999,1,1)
ajay=Person('ajay','india',ajaydob)
ajay.age()

class Calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        c=self.a+self.b
        print(c)
#Write a Python program to create a class that represents a shape. Include methods to calculate its area
# and perimeter. Implement subclasses for different shapes like circle, triangle, and square
class Shape():
    def __init__(self):
        pass
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r=r

    def area(self):
        a=3.12*self.r**2
        print('area of circle', a)
    def perimeter(self):
        p=2*3.14*self.r
        print('perimeter of circle', p)

c=Circle(4)
c.area()
c.perimeter()
