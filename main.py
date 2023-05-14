import ChatAPI as chat
from ChatException import ChatException
from chatmodels import inputs as iomodels

# import History as history
def main():
    try:
        # initiate loop
        loop = True
        # set defaults
        save_chat = False
        model = 1

        # show the model choices
        for m, n in iomodels.items():
            print(f'{n}. {m}')
        # allow the user to pick a model (or not)
        model = int(input('Choose a completion model (or leave blank for default model '))
        # quick and dirty method to make sure the model is in the choices
        if model < 1 or model > 5:
            model = 1
        
        # ask if user wants to save the chat as a file
        if input('Would you like to store the chat history? (y/n) ') == 'y':
            save_chat = True
            file_name = input('What is the name of the file where you want to save the history? ')
            # force filename to end in .txt so it is saved as a text file
            if not file_name.endswith('.txt'):
                file_name = file_name + '.txt'
            # instantiate the chat with all of the choices.
            c = chat.Chat(model = model, with_history = save_chat, file_name = file_name)
        else:
            # taske the default, no history chat
            c = chat.Chat(model = model)

        # start asking questions and getting answers
        while loop:
            question = input('What question would you like to ask? (Leave blank to quit)')
            if question == '':
                loop = False
                c.quit()
                break
            print(c.ask(question))
    except ValueError as err:
        print('The input given was not accepted.', err)
    except ChatException as err:
        print('There was a problem communicating with openai.')
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise



if __name__ == '__main__':
    main()
