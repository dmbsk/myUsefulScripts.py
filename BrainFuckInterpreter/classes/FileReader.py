import os
class FileReader:
    def __init__(self):
        self.file = ''
        self.data = []
        self.filePath = './helloword.bf'

    def setFilePath(self, newFilePath):
        self.filePath = newFilePath

    def read(self):
        self.file = open(self.filePath, 'r')

    def loadData(self):
        if self.file is not '':
            self.data = self.file.readlines()
            return self.data
        else:
            return print("FileReader can not read file (is None)")
