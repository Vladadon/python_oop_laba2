class User:
    name = 'oop python'
    def show(self):
        return self.cape(self.name)

    def cape(self,stri):
        return stri.upper()
    
class Student:
    name = "Amog"
    surname = "Us"
    def fun1(self):
        print(self.name)
student = Student()
student.fun1