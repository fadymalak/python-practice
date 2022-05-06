from typing import Protocol


class Email(Protocol):
    """
    this type hint called protocol
    this tell mypy any class or subclass of Email should support :attr: email and should be str
    """

    email: str


class Account:
    def __init__(self, email: str) -> None:
        self.email = email


class MailSender(Account, Email):
    def __init__(self, email) -> None:
        super().__init__(email)

    def send_mail(self, message: str) -> None:
        print(f"sending mail to {self.email}")


mail = MailSender(email="fady.malak.awad@gmail.com")
mail.send_mail("hello friend")
