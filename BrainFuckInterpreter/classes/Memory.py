class Memory:
    def __init__ (self):
        self.data = []
        self.size = 32
        self.index = 0

    def setMemorySize(self, size): # set memory size
        self.size = size

    def getMemorySize(self): # return momory size
        return self.size

    def alocateMemory(self): # alocate memory
        for i in range(0, self.size):
            self.data.append(0)

    def incrementPointer(self):
        self.data[self.index] += 1

    def decrementPointer(self):
        self.data[self.index] -= 1

    def moveIndex(self, direction):
        if (direction is 'r' and self.index is self.size) or (direction is 'l' and self.index is 0):
            return 'Out of bounds'
        else:
            if direction is 'r' and self.index is not self.size:
                self.index += 1
            elif direction is 'l' and self.index is not 0:
                self.index -= 1

    def printPointer(self):
        print(chr(self.data[self.index]), end='')

    def userDataInput(self):
        self.data[self.index] = input()