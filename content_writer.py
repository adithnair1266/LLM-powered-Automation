from agents import Agent
from tools import Tools
from termcolor import colored
import json
import sys
from prompts import *
query = input("Enter the topic to search on: ")

#To optimize search query to yield latest results
searchEngineAgent = Agent(
    model = "mixtral-8x7b-32768",
    systemPrompt= searchAgentPrompt ,
    server = "groq"
)



searchQuery = searchEngineAgent.runAgent(query)
data = json.loads(searchQuery)
searchQuery = data.get("response", None)
print(colored(searchQuery, "blue"))
x = bool(input("Do you wish to proceed? "))

#To check if returned search query is satisfied
if x == False:
    sys.exit()

#Fetching the URLs using Serper API
urls = Tools.fetch_urls(searchQuery, 5)
print(colored(urls, "yellow"))



#To check what kind of scraping is to be done (Newspaper3k scraping for news articles)
scrape_type = bool(input("Do you want to fetch news articles: "))
if scrape_type == False:
    content_old = Tools.scrape_all_urls(urls)
else:
    articles = Tools.extract_multiple_articles(urls)
    content_old = "\n\n".join(articles.values())

#Save scraped content in a file
Tools.save_text_to_file(content_old, query, "txt", "D:/projects/Agents/myAgents/scrapedTexts")

#Fetch scraped content from a file
content = Tools.read_text_from_file(f"{query}.txt", "D:/projects/Agents/myAgents/scrapedTexts")

#Ask user what kind of content to be written(blog, news article, even poems)
#Can include the word length for the required content
type = input("Enter the type of content to create: ")

writerAgent = Agent(
        model = "mixtral-8x7b-32768",
        systemPrompt= f"""
        You are a creative writer for a news company. Based on only the context, {content}, answer the query in a clear
        concise manner, Use search engine optimised words to grab the attention of the readers, include direct texts
        from the context, and include a introductory paragraph and finish with an imaginative conclusion.
        Do not your background knowledge, only use what is provided in the content,""",
        server = "groq"
)


article = writerAgent.runAgent(f"Write a {type} on {query}")

#To save the article in a separate file
saved = input("Do you want to save it to the cloud? ")
if saved == "yes":
    Tools.save_text_to_file(article,query,"docx", "D:/nextcloudStorage/Documents/Auto_blogs")
else:
    print("Did not save!")

