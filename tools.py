import requests
from newspaper import Article
from termcolor import colored
import os
from dotenv import load_dotenv

load_dotenv()

import json
from bs4 import BeautifulSoup
import re
class Tools:
    
    #Function to fetch news URLs from Serper API
    def fetch_urls(query,num = 3):
        url = "https://google.serper.dev/search"
        api_key = os.getenv("SERPER_API_KEY")
        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }
        params = {
            "q": query,
            "location": "India",
            "tbm": "nws",  
            "num": num
        }
        
        response = requests.post(url, headers=headers, json=params)

        
        if response.status_code == 200:
            data = response.json()
            urls = [result['link'] for result in data.get('organic', [])]
            return urls
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    #Function to extract content from one article using Newspaper3k
    def extract_article_text(url):
        try:
            headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            article = Article(url)
            article.set_html(response.text)
            article.parse()
            
            return article.text
        except Exception as e:
            print(f"Failed to extract article from {url}. Error: {e}")
            return None
        
    #Function to extract content from multiple articles using Newspaper3k
    def extract_multiple_articles(urls):
        articles_text = {}
        for url in urls:
            text = Tools.extract_article_text(url)
            if text:
                articles_text[url] = text
        return articles_text
    

    #Function to save the scraped content to a text file
    def save_text_to_file(text, filename, ext,directory=None):
        try:
            if directory:
                # Ensure the directory exists
                os.makedirs(directory, exist_ok=True)
                # Combine the directory and filename to get the full path
                full_path = os.path.join(directory, filename)
            else:
                # If no directory is provided, use the filename as is
                full_path = filename
            
            with open(f"{full_path}.{ext}", 'w', encoding='utf-8') as file:
                file.write(text)
            print(f"Text successfully saved.")
        except Exception as e:
            print(f"An error occurred while saving text to the file: {e}")


    #Function to read content from a file
    def read_text_from_file(filename, directory=None):
        try:
            if directory:
                # Combine the directory and filename to get the full path
                full_path = os.path.join(directory, filename)
            else:
                # If no directory is provided, use the filename as is
                full_path = filename
            
            with open(full_path, 'r', encoding='utf-8') as file:
                text = file.read()
            return text
        except Exception as e:
            print(f"An error occurred while reading text from the file: {e}")
            return None

    #Funtcion to scrape website using BeautifulSoup
    def scrape_and_clean(url):
    # Make the HTTP request to the specified URL with optional headers
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        

            
    
        
        # Function to clean the content
        def clean_content(content):
            # Remove unwanted tags like script, style, etc.
            for tag in content(['script', 'style', 'header', 'footer', 'nav', 'aside']):
                tag.decompose()
            
            # Extract and clean the text
            cleaned_text = content.get_text(separator='\n', strip=True)
            text = re.sub(r'\s+', ' ', cleaned_text)
            
            # Remove leading and trailing white spaces
            text = text.strip()
            
            # Split the text into lines, remove empty lines, and join back
            lines = text.split('\n')
            cleaned_lines = [line.strip() for line in lines if line.strip()]
            
            # Join the cleaned lines back into a single string
            cleaned_text = '\n'.join(cleaned_lines)
                
            return cleaned_text
                

        cleaned_text = clean_content(soup)
        
        return cleaned_text
    
    # Function to scrape multiple URLS
    def scrape_all_urls(urls):
        content = ''
        for url in urls:
            
            try:
                newContent = Tools.scrape_and_clean(url)
                content = content + newContent +'\n\n'
            except Exception as e:
                print(colored(f"Error occured while scraping, {e}", "red" ))
        print(colored(content, "light_cyan"))
        return content

