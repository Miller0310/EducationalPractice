from practice_4_utils import isArmstrong


class Iterator:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        a = self.num
        while True:
            a += 1
            if isArmstrong(a):
                self.num = a
                return a
