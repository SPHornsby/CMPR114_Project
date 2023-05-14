import openai
import json
import os
from dotenv import load_dotenv
import History as history

load_dotenv()
COMPLETION_URL = 'https://api.openai.com/v1/chat/completions'
MODEL='text-davinci-003'
openai.organization = "org-aDyo6jEbWJVp1yvaaDJqlcwU"
openai.api_key = os.getenv("OPENAI_API_KEY")

class Chat:
    def __init__(self, model = 'text-davinci-003', with_history = False, file_name = 'default.txt'):
        self.__model = model
        self.__history = None
        if with_history:
            self.__history = history.History(file_name)
    
    def ask(self, question):
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
        response = response['choices'][0]['text']
        if not self.__history == None:
            self.__history.addToHistory(('question: '+ question.strip()))
            self.__history.addToHistory(('response: '+ response.strip()))

        return response
    def quit(self):
        if not self.__history == None:
            self.__history.saveHistory()
        