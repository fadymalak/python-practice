class User:
    name = "fady"

    def __init__(self):
        self.name2 = "Asdasd"


print(User().__dict__)  # instance __dict__
print(User.__dict__)  # class __dict__
