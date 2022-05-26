from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    email: str


x = User(id=1, username="hello", email="email.com")
print(x.username)
print(x.id)
