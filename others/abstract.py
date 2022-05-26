from abc import ABC, ABCMeta, abstractmethod
from typing import Union, final, List, Any


class FileLoader(ABC):
    __metaclass__ = ABCMeta

    def __init__(self, fname: str) -> None:
        self._fname: str = fname
        self._data: Union[str, List[Any]] = ""

    @abstractmethod
    def load(self) -> None:
        ...

    @abstractmethod
    def show(self, start: int, end: int) -> Union[str, List[Any]]:
        ...

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value) -> None:
        self._length = value


class TextLoad(FileLoader):
    def load(self) -> None:
        with open(self._fname, "r") as f:
            self._data = f.readlines()
        self._length = len(self._data)

    def show(self, start: int = 0, end: int = -1) -> Union[str, List[Any]]:
        data = self._data[start:end]
        print(data)
        return data


txt = TextLoad("file.txt")
txt.load()
txt.show(end=1)
