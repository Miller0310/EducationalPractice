class Logger:
    def __init__(self, file):
        self._file = file

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self,value):
        self._file = value

    def printToFile(self, name, dictionary):
        file = open(self._file, 'a')
        file.write(name+':'+str(dictionary)+'\n')
        file.close()
