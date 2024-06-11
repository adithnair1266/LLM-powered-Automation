import requests
from termcolor import colored
import json
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

class Agent:
    """
    Depending upon the inference servers, three options available:
    1. Groq: Quick, efficient, requires API Key
    2. Ollama: Local, needs to download ollama from official Website
    3. LM : local, can use any Huggingface Model, supported by LM studio for inference

    """
    headers = {"Content-Type": "application/json"}

    def __init__(self,model,systemPrompt,server ):

        
        self.model = model
        self.systemPrompt =  systemPrompt
        self.server = server

    def runAgent(self, query):
        #Ollama Server
        if self.server == "local":
            endpoint = 'http://localhost:11434/api/generate'
            payload = {
                "model": self.model,
                "prompt": query,
                "system": self.systemPrompt,
                "stream": False,
                "temperature": 0,
            }
            try:
                response = requests.post(endpoint, headers=self.headers, data=json.dumps(payload))
                response_dict = response.json()


                response = response_dict['response']
                print(colored(f"Output: {response}", 'green'))

                return response

            except Exception as e:
                print("Error in response:", response_dict)

                return None
            

        #Groq Server
        elif self.server == "groq":
            client = Groq(api_key= os.getenv("GROQ_API_KEY"))
            chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": self.systemPrompt,
                        },
                        {
                            "role": "user",
                            "content": query,
                        }
                    ],
                    model="llama3-8b-8192",
                )
            response = chat_completion.choices[0].message.content
            print(colored(f"Output: {response}", "green"))
            return response
        


        #LM Studio
        elif self.server == "LM":
            from openai import OpenAI
            client = OpenAI(base_url="http://localhost:8001/v1", api_key="lm-studio")

            completion = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.systemPrompt},
                {"role": "user", "content": query}
            ],
            temperature=0.7,
            )

            print(colored(completion.choices[0].message.content, "green"))

            return completion.choices[0].message.content




