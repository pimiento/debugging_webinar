#!/usr/bin/env python3
from dataclasses import dataclass
@dataclass
class MyObj:
    n: int
    def go(self):
        for i in range(self.n):
            print(i)
if __name__ == "__main__":
    MyObj(5).go()
