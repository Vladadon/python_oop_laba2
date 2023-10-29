class User:
    __name = None
    __surname = None

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname


user = User('john', 'smit')
print(user.getName())
print(user.getSurname())
