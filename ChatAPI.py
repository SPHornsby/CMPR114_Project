import openai
import json
import os
from dotenv import load_dotenv
import History as history
from ChatException import ChatException
import time
from chatmodels import chats as cm

load_dotenv()
COMPLETION_URL = 'https://api.openai.com/v1/chat/completions'
# MODEL='text-davinci-003'
openai.organization =  os.getenv("OPENAI_API_ORG")#"org-aDyo6jEbWJVp1yvaaDJqlcwU"
openai.api_key = os.getenv("OPENAI_API_KEY")

class Chat:
    '''Chat wraps the openai library to provide access to the chatCompletion methods.'''
    def __init__(self, model = 1, with_history = False, file_name = 'default.txt'):
        self.__model = cm[model]
        self.__history = None
        if with_history:
            self.__history = history.History(file_name)

    def chat(self, question:str)->str:
        try:
            start = time.time()
            response =openai.ChatCompletion.create(
                model=self.__model,
                messages=[
                    {'role':'user', 'content':question}
                ]
            )
            end = time.time()

            usage = response['usage']
            total_tokens = usage['total_tokens']
            print(f'Total tokens used for this question: {total_tokens}')
            response = response['choices'][0]['message']['content']
            if not self.__history == None:
                self.__history.addToHistory((str(start),': Question: '+ question.strip()))
                self.__history.addToHistory((str(end),': Response: '+ response.strip(), ', response time: ' + str(round(end - start, 2))))
                self.__history.addToHistory('total tokens used: '+str(total_tokens))
            return response
        except openai.error.RateLimitError as err:
            time.sleep(10)
            return 'The question could not be asked because the rate limit was exceeded. Please try again.'
        except:
            raise ChatException
    def ask(self, question):
        try:
            start = time.time()
            response = openai.Completion.create(
                model=self.__model,
                prompt=f"Q: {question}\nA:",
                # temperature=0,
                # max_tokens=100,
                # top_p=1,
                # frequency_penalty=0.0,
                # presence_penalty=0.0,
                stop=["\n"]
            )
            end = time.time()
            response = response['choices'][0]['text']
            if not self.__history == None:
                self.__history.addToHistory((str(start),': Question: '+ question.strip()))
                self.__history.addToHistory((str(end),': Response: '+ response.strip(), ', response time: ' + str(round(end - start, 2))))

            return response
        except Exception as err:
            print(err)
            raise ChatException()
    def quit(self):
        if not self.__history == None:
            self.__history.saveHistory()
        