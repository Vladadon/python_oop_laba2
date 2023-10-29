class User:
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name


class Student(User):
    def setYear(self, year):
        self._year = year

    def getYear(self):
        return self._year


class StudentProgrammer(Student):
    def setSkill(self, skill):
        self._skill = skill

    def getSkill(self):
        return self._skill