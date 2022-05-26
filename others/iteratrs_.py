from typing import Iterable, Iterator


class TextIterable(Iterable[str]):
    """Iterable is an object with elements"""

    def __init__(self, text):
        self.text = text

    def __iter__(self):
        return TextIterator(self.text)


class TextIterator(Iterator[str]):
    def __init__(self, itr):
        self.itr = itr.split(" ")
        self._index = -1

    def __next__(self):
        self._index += 1
        if self._index < len(self.itr):
            return self.itr[self._index]
        else:
            raise StopIteration()


x = iter(TextIterable("f a d y"))
try:
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
except StopIteration:
    pass

for i in TextIterable(" ".join(["s", "a", "w"] * 2)):
    print(i)


class A:
    def run(self):
        print("A")
        return "A"


class B:
    def run(self):
        print("B")
        return "B"
