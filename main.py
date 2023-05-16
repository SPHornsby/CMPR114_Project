import ChatAPI as chat
from ChatException import ChatException
from chatmodels import inputs as iomodels
# import time

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
        model_answer = input('Choose a completion model ')
        if type(model_answer) is not int:
            model = 1
        model = int(model)
        # quick and dirty method to make sure the model is in the choices
        if model not in iomodels.values():
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
        # lastThreeTimes = []
        while loop:
            
            question = input('What question would you like to ask? (Leave blank to quit)')
            if question == '':
                loop = False
                c.quit()
                break
            # qtime = time.time()
            # if len(lastThreeTimes)> 3:
            #     lastThreeTimes.pop(0)
            # lastThreeTimes.append(qtime)
            # if len(lastThreeTimes) >= 3:
            #     timeGap = lastThreeTimes[3] - lastThreeTimes[0]
            #     print(timeGap)
            #     if timeGap < 30:
            #         time.sleep(30 - timeGap)
            print(c.chat(question))
    except ValueError as err:
        print('The input given was not accepted.', err)
    except ChatException as err:
        print('There was a problem communicating with openai.')
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise



if __name__ == '__main__':
    main()
