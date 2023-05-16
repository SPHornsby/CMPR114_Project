import History as history


class TestHistory:
    def test_addToHistory(self):
        testHistory = history.History('test_file.txt')
        line_to_add = 'test line'
        testHistory.addToHistory(line_to_add)
        assert line_to_add in testHistory.getChat()

    def test_saveFile(self):
        testHistory = history.History('test_file.txt')
        line_to_add = 'test line'
        testHistory.addToHistory(line_to_add)
        testHistory.saveHistory()
        fh = open('test_file.txt', 'r')
        fh.close()
    
    
