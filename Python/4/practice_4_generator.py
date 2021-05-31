from practice_4_utils import isArmstrong


def generator():
    a = 0
    while True:
        a += 1
        if isArmstrong(a):
            yield a
