from agents import Agent
from tools import Tools

programmer = Agent(model="llama3-70b-8192",
            systemPrompt= "You are a useful AI Code assistant. Answer based on \
                the input query.Return only the code, do not explain.\
                ",
            server = "groq")

s = programmer.runAgent(input("Enter query: "))

# String formatting to remove first and last line
content = s[s.find('\n')+1:s.rfind('\n')]

Tools.save_text_to_file(content, input("Enter filename: ") , input("Enter extension: ") , "D:/projects/Agents/myAgents/auto_code" )