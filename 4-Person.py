# #                                       4. Person
# # Create a Python class Person with attributes: name and age of type string.
# # Create a display() method that displays the name and age of an object created via the Person class.
# # Create a child class Student which inherits from the Person class and which also has a section 
# # attribute.
# # Override the method display() for the Student class. Make it such that it displays the name, age 
# # and section of an object created via the Student class.
# # Create Person and Student objects and then test the display() method for both.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print( "Name:{} and Age:{}".format(self.name,self.age))
    
class Student(Person):
    def __init__(self,name,age,section):
        super().__init__(name,age)
        self.section=section
    
    def display(self):
        print(f"Name:{self.name} and Age:{self.age} and Section:{self.section}")

object_1=Person("Mary Johnson","25")
object_2=Student("Peter Mate","21","Mathematics")

object_1.display()
object_2.display()




