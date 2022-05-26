from collections import Counter, defaultdict, ChainMap, UserDict, UserString
from typing import (
    Any,
    Callable,
    Iterable,
    Iterator,
    Tuple,
    Union,
    Set,
    List,
    NamedTuple,
    Mapping,
    Counter,
)

"""
 from py 3.7 no need to use to use OrderedDict
    earlier it was hard to predict ordering of dict

    1- Counter
    2- defaultdict
"""
l: list[int] = [1, 2, 1, 2, 3, 5, 6, 7, 1, 1]
l2: str = "asdabdsatgsg"
# Counter(Iteration[Union[list,set,tuple,str]])
count: Counter = Counter(l2)

print(count["a"])
# return of most common items
# list[set(Union[str,int],int)]
common: List[Tuple[str, int]] = count.most_common(2)
print(common[1])
###############################################
print("########## defaultdict ###########")
dd: defaultdict = defaultdict(int)
dd["a"] = 2
print(dd)
print(dd.items())
dd2: defaultdict = defaultdict(lambda: defaultdict(int))  # defaultdict(Callable)
dd2["jan"]["a"] = 2
print(dd2)
