
class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_name(self):
        return self.name.upper()

    def age(self, current_year):
        return current_year - self.birth_year


user = User("John", 2001)
print(user.age(2024))
print(user.get_name())
