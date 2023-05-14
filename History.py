import os

class History:
    def __init__(self, fileName = None):
        self.__chat = []
        self.__fileName = fileName

    def addToHistory(self, line):
        try:
            self.__chat.append(line)
        except:
            print('There was a problem storing the last line. The chat transcript may not be complete.')

    def saveHistory(self):
        try:
            fh = open(self.__fileName, 'a')
            for line in self.__chat:
                fh.write(line + '\n')
            fh.close()
        except Exception as e:
            print('There was an problem saving the file.')
            exit(1)