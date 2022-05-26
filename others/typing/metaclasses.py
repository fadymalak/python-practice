import logging
import abc
from functools import wraps
from typing import cast


class DiceMeta(abc.ABCMeta):
    def __new__(mcls, name, bases, namespace, **kwargs) -> "DiceMeta":
        super().__new__(mcls, name, bases, namespace, **kwargs)
        if "roll" in namespace and not getattr(
            namespace["roll"], "__isabstractmethod__", False
        ):
            namespace.setdefault("logger", logging.getLogger(name))
            func = namespace["roll"]

            @wraps(func)
            def logged_roll(self) -> None:
                func(self)
                self.logger.info(f"Rolled {self.face} ")

            namespace["roll"] = logged_roll

        new_object = cast("DiceMeta", abc.ABCMeta.__new__(mcls, name, bases, namespace))
        return new_object
        # super().__new__(mcls,name,bases,namespace)
