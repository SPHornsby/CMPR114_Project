import ChatAPI as chat
# import History as history
def main():
    
    loop = True
    save_chat = False
    if input('Would you like to store the chat history? (y/n) ') == 'y':
        save_chat = True
        file_name = input('What is the name of the file where you want to save the history? ')
        if not file_name.endswith('.txt'):
            file_name = file_name + '.txt'
        c = chat.Chat(with_history = save_chat, file_name = file_name)
    else:
        c = chat.Chat()
    while loop:
        question = input('What question would you like to ask? (Leave blank to quit)')
        if question == '':
            loop = False
            c.quit()
            break
        print(c.ask(question))
    
main()

# ch = history.History('test.txt')
# line1 = '4'
# line2 = '5'
# line3 = '6'
# ch.addToHistory(line1)
# ch.addToHistory(line2)
# ch.addToHistory(line3)
# ch.readHistory()
# # ch.saveHistory()

