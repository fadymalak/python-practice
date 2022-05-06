from __future__ import annotations


class Contacts:
    def __init__(self, name: str = "Test") -> None:
        self.name = name


class Contactsx:
    def __init__(self) -> None:
        self.w = "w"


class C(list["Contacts"]):
    """
    inheritance from list  built-in type
    """

    pass


con = Contacts()
c = C()
c.append(con)
print(c)
