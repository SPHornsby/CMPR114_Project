import os

class History:
    '''This class deals with storing the chat history in local memory and then persisting it to a file. '''
    def __init__(self, fileName = None):
        self.__chat = []
        self.__fileName = fileName

    def addToHistory(self, line):
        try:
            self.__chat.append(line)
        except:
            print('There was a problem storing the last line. The chat transcript may not be complete.')

    def saveHistory(self)->None:
        try:
            fh = open(self.__fileName, 'a')
            for line in self.__chat:
                if type(line) is tuple:
                    line = convertTuple(line)
                if type(line) is not str:
                    raise ValueError('Chat could not be converted to string')
                fh.write(line + '\n')
            fh.close()
        except Exception as err:
            print(err)
            print('There was a problem saving the file.')
            exit(1)
    def getChat(self):
        return self.__chat
    
def convertTuple(tup:tuple)->str:
    '''Converts a tuple into a concatenated string'''
    # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str