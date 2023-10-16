class User:
    None
class Employee:
    name = None
    salary = None
    age = None

employee1 = Employee()
employee2 = Employee()
employee1.name = "Bob"
employee1.salary = 300
employee1.age = 20
employee2.name = "Stiv"
employee2.salary = 400
employee2.age = 25
print(employee1.salary)
print(employee2.salary)

user1 = User()
user2 = User()
user1.name = 'john'
user2.name = 'eric'
print(user1.name)
print(user2.name)