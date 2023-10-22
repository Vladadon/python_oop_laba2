class User:
  name = None

  def show(self):
    print(self.name)
user = User()
user.name = 'john'
user.show()

class Employee:
    name = 'SussyBaka'
    salary = '300$'

    def show1(self):
       print(self.name)
    def show2(self):
       print(self.salary)
employee = Employee()
employee.show1()
employee.show2()