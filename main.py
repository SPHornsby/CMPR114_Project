import ChatAPI as chat
from ChatException import ChatException

# import History as history
def main():
    try:
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
    except ValueError as err:
        print('The input given was not accepted.')
    except ChatException as err:
        print('There was a problem communicating with openai.')
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
main()


if __name__ == '__main__':
    main()
