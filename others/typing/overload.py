from typing import overload, Any, Union

"""
typing.overload :
    provide  multi type-check variants for same function
    ie: >> if param:int will return int line 10
        >> if param:str will return str line 15 
"""


@overload
def tes(i: int) -> int:
    ...


@overload
def tes(i: str) -> str:
    ...


def tes(i: Any) -> Union[int, str]:
    return i


tes("s")
tes(1)
tes(
    [
        "a",
    ]
)  # mypy: Error  param:list  not in possible overload variants
