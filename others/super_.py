class Quiz:
    def __init__(self, qid: int) -> None:
        self.qid = qid


class Question:
    def __init__(self, title: str, answer: str) -> None:
        self.title = title
        self.answer = answer


class YNQuestion(Question):
    def __init__(self, title: str, answer: str) -> None:
        super().__init__(title, answer)
        self.qtype = "Yes&No"


class GQuestion(Question, Quiz):
    """
    Multi inheritance initilization
     >> Class1.__init__(self , *args)
     >> Class2.__init__(self , *args)
    """

    def __init__(self, title: str, answer: str, qid: int) -> None:
        Question.__init__(self, title, answer)
        Quiz.__init__(self, qid)
        self.qtype = "General"


Q1 = YNQuestion(title="Title1", answer="Answer1")
Q2 = GQuestion(title="Title2", answer="Answer2", qid=5)
print(Q2.qid)
print(Q1.answer)
