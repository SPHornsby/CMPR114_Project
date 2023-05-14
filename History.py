import os

class History:
    def __init__(self, fileName = None):
        self.__chat = []
        self.__fileName = fileName
        if fileName != None and os.path.isfile('./' + fileName):
            fh = open(fileName, 'r')
            for line in fh:
                self.addToHistory(line)
            fh.close()

    def addToHistory(self, line):
        self.__chat.append(line)
    
    def readHistory(self, number_of_lines=0):
        if number_of_lines == 0:
            for line in self.__chat:
                print(line+'\n')
    
    def saveHistory(self):
        fh = open(self.__fileName, 'a')
        for line in self.__chat:
            fh.write(line)
        fh.close()