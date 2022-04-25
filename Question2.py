#                               2. Rectangle
#   Write a Rectangle class, allowing you to build a rectangle with length and width attributes.
#   Create a perimeter() method to calculate the perimeter of the rectangle and an area() method to
# calculate the area of ​​the rectangle.
#   Create a method display() that displays the length, width, perimeter and area of an object created
# using an instantiation on Rectangle class.
#   Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute 
# and another volume() method to calculate the volume of the Parallelepiped.



class Rectangle:
    def __init__(self,length,width):
           self.lenght=length
           self.width=width
    
    def perimeter(self):
        return 2 * (self.lenght + self.width)

    def area(self):
        return self.lenght * self.width
    
    def display(self):
        return "Perimeter:{} and Area:{}".format(Rectangle.perimeter(self),Rectangle.area(self))

class Parallelepipede(Rectangle):
    
    def __init__(self,lenght,width,height):
        super().__init__(lenght,width)
        self.height=height

    def volume(self):
        return self.lenght*self.width*self.height

object_1=Rectangle(12,13)
print(object_1.display())

object_2=Parallelepipede(10,15,10)
print(object_2.volume())