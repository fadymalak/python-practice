"""
Notice that  
    when we try to access attributes python check it first if it exists in 
    Instance scope if not then check class scope

"""


class User:
    name = "fady_cls"

    @property
    def full_name(self):
        # look it search for instance attribute
        print(self.name)


f = User()
f.full_name


class User2:
    name = "fady_cls"

    def __init__(self):
        self.name = "fady_init"

    @property
    def full_name(self):
        print(self.name)


f2 = User2()
f2.full_name
