import pickle
from threading import Timer
import datetime
import time


class PrintRepeater:
    def __init__(self) -> None:
        self.timer: Timer
        self.last_update: datetime.datetime
        self.run()

    def run(self, v: str = "__init__") -> None:
        self.schedule()
        for i in range(2):
            print("hello world from  ", v)
            time.sleep(2)

    def schedule(self) -> None:
        self.timer = Timer(
            1,
            self.run,
            [
                "thread",
            ],
        )
        # if daemon set to False  thread will not exit when main thread exit
        # you should kill it yourself
        self.timer.daemon = False
        self.timer.start()


printer = PrintRepeater()
print("exit")
