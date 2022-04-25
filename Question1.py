#                                1-School
# Create a School class with instance attribute capacity.
# Add students as the class attribute. This will be a list and keep track of the students in the school.
# Create a Student class with attributes: name, age, gender
# Add __str__ method to this class to print the objects.
# Add add_student method to the class. If capacity is full print error message else add the student.
# Add print_students method to print the all existing students. Loop through the students list and
#    print each student object.
# Create a School object and threee students, add first 2 students to school. Print students and afterwards try to add the third student.
# Use __dict__ method to see attributes

class School:
    students=[]

    def __init__(self,capacity):
        self.capacity=capacity

    def add_student(self,student):
        if len(self.students)==self.capacity:
            print("THe capacity is full!")
        else:
            self.students.append(student)
            print("The student was appended")

    def print_student(self):
        for student in self.students:
            print(student)

       
class Student:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def __str__(self):
        return f" {self.name} is {self.age} old and {self.gender}"


mySchool=School(2)
student_1=Student("Eva",21,"female")
student_2=Student("Alice",23,"female")
student_3=Student("Jack",25,"male")

mySchool.add_student(student_1)
mySchool.add_student(student_2)
mySchool.add_student(student_3)  # Won't allows me to add because the capacit was identifed as 2

print(student_1) # I used attribute of "__str__ "
print(student_2)

mySchool.print_student()  #It was weird:it returns same output with __str__ method.If classes don't includes of__str__ turns an adress of an object
print(student_1.__dict__)
print(mySchool.__dict__)







        





        

