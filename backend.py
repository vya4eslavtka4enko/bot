import openai
from openai import OpenAI
import os
class Chatbot:
    def __init__(self):
        # openai.api_key = os.environ['OPENAI_API_KEY']
        openai.api_key = ""
        # client = OpenAI(api_key="<API_KEY>")
    def get_response(self,user_input):
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt="Say this is a test",
            max_tokens=5,
            temperature=0
        ).choices[0].text
        return response

if __name__ == '__main__':
    chatbot = Chatbot()
    response = chatbot.get_response("Write the joke about bird")
    print(response)