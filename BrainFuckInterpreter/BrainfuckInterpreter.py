from classes.Memory import Memory
from classes.bcolors import bcolors
# from classes.FileReader import FileReader fix needed

def minify(data):
    mindata = ''
    for i in range(0, len(data)):
        mindata += data[i].replace('\n', '')

    mindata.replace(' ', '')
    return mindata

file = open('./simpletest.bf', 'r')  # output should be wtyq
fileData = file.readlines()

warrning = []
fail = []

memory = Memory()
memory.setMemorySize(16)
memory.alocateMemory()


for i in range(0, len(fileData)):
    for j in range(0, len(fileData[i])):
        if fileData[i][j] is '+':
            memory.incrementPointer()
        elif fileData[i][j] is '-':
            memory.decrementPointer()
        elif fileData[i][j] is '>':
            memory.moveIndex('r')
        elif fileData[i][j] is '<':
            memory.moveIndex('l')
        elif fileData[i][j] is '.':
            memory.printPointer()
        elif fileData[i][j] is ',':
            memory.userDataInput()
        # elif fileData is '[':
        #     memory.startLoop()
        # elif fileData is '}':
        #     memory.endLoop()
        elif fileData[i][j] not in [' ', '\n']:
            warrning.append("Uknown character at line [" + str(i) + "] and index [" + str(j) + "}")

print('\n\n')
for i in range(0, len(warrning)):
    print(bcolors.WARNING + str(warrning[i]) + bcolors.ENDC)
for i in range(0, len(fail)):
    print(bcolors.FAIL + str(fail[i]) + bcolors.FAIL)