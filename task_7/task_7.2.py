class Users:
    name = None

    def show(self):
        print(self.name)


user = Users()

user.name = "john"

user.show()


class Employee:
    name = None
    salary = None

    def name(self):
        name = None

    def salary(self):
        salary = None

    def display_info(self):
        print(f"имя: {self.name}")
        print(f"зарплата: {self.salary}")


worker = Employee()

worker.name = "misha"
worker.salary = "23000 руб."

worker.display_info()
