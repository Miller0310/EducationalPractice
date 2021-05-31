from Validator import Validator
validator = Validator()


class Read:
    @staticmethod
    def insert(array):
        file_name = input("Enter file name: ")
        position = validator.integer(input("Enter position: "))
        with open(file_name, 'r') as stream:
            for line in stream:
                array.Insert(position, int(line))
        return array
