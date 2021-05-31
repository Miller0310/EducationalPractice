from practice_4_iterator import Iterator
from Validator import Validator

iterator = Iterator()
validator = Validator()


class Generate:
    @staticmethod
    def insert(array):
        print("Enter position to insert: ",end='')
        pos = validator.integer(input())
        element = next(iterator)
        array.Insert(pos, element)
        return array
