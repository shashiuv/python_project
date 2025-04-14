class Person:
    def __init__(self,name,age,):
                        
        self.name = name
        self.age = age

    def display(self):

        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

class student(Person):
    def __init__(self,name,age,dpm=''):
        super().__init__(name,age)
        self.dpm = dpm
    def display(self):
        super().display()
        if self.dpm :
             print(f"Department: {self.dpm}")
        else:
            print(f"Deparyment: Arts")

p1 = Person("John",45)
p1.display()

st1 = student("Paul",23)
st1.display()
