class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks  # private attribute
        
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.__marks}")
            
    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if self.__marks > 0:
            self.__marks=marks
        else:
            self.__marks=0
            
s1 = Student("janar",526)
s1.display()
            
        