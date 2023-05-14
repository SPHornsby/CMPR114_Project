import openai
import json
import os
from dotenv import load_dotenv
import History as history
from ChatException import ChatException
import time
import chatmodels as cm

load_dotenv()
COMPLETION_URL = 'https://api.openai.com/v1/chat/completions'
MODEL='text-davinci-003'
openai.organization = "org-aDyo6jEbWJVp1yvaaDJqlcwU"
openai.api_key = os.getenv("OPENAI_API_KEY")

class Chat:
    def __init__(self, model = 1, with_history = False, file_name = 'default.txt'):
        self.__model = cm[model]
        self.__history = None
        if with_history:
            self.__history = history.History(file_name)
    
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
        