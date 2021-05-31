class Validator:
    @staticmethod
    def integer(value):
        try:
            return int(value)
        except TypeError:
            raise TypeError
