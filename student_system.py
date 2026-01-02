class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def display(self):
        print(f"name:{self.name},marks:{self.marks}")

s1=Student("janar",526)
s1.display()