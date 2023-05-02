import sys
import urllib.parse
import random
import os
import requests
import openai
import openai
import re
import tiktoken
from bs4 import BeautifulSoup, Comment
from urllib.parse import urlparse
from unidecode import unidecode

# Setup OpenAI API credentials
openai.api_key = os.environ.get("OPENAI_API_KEY")
MAX_TOKENS = 3584
MODEL = "gpt-3.5-turbo"
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
# Define a function to crawl a website for relevant content
def crawl(url, visited=None):
    if visited is None:
        visited = set()
    visited.add(url)

    # Extract the domain name from the URL
    domain_name = urlparse(url).netloc    
    response = requests.get(url, headers=HEADERS)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    print("\n== " + url)
    print("== " + soup.title.string)

    # Get the links, ignore dupes or visited
    links = set()
    for link in soup.find_all('a'):
        href = link.get('href')
        if (href is None) :
            continue        
        if href.startswith('/'):
            href = urlparse(url)._replace(path=href).geturl()
        
        uri = urlparse(href)
        href = uri.scheme + '://' + uri.netloc + uri.path

        if uri.netloc == domain_name and href not in visited:
            links.add(href)
        link.decompose() # remove the link

    # Remove ads, menus, footers by finding and removing elements with certain classes or IDs
    for noise in soup.select(".ad, #ad, .ads, #ads, .menu, #menu, .nav, #nav, .footer, #footer, .copy, #copy"):
        noise.decompose()
    for tag in soup.find_all(["form","iframe","noscript","img","script", "style", "meta", "link", "input", "button", "select", "textarea"]):
        tag.decompose()
    for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
        comment.extract()

    # Break the content down to work under the max tokens
    # Now remove all links
    # Extract text from document
    # text = soup.prettify();
    text = unidecode(soup.get_text(separator='\n')).strip()
    text = re.sub(r'\n+', '\n', text)
    
    # Summarize
    summarize(text)
    # print(text)

    # Recursively scrape content from each link
    # for link in links:
    #     crawl(link, visited=visited)
    
def create_chunks(text, n, tokenizer):
    tokens = tokenizer.encode(text)
    i = 0
    while i < len(tokens):
        # Find the nearest end of sentence within a range of 0.5 * n and 1.5 * n tokens
        j = min(i + int(1.5 * n), len(tokens))
        while j > i + int(0.5 * n):
            # Decode the tokens and check for full stop or newline
            chunk = tokenizer.decode(tokens[i:j])
            if chunk.endswith(".") or chunk.endswith("\n"):
                break
            j -= 1
        # If no end of sentence found, use n tokens as the chunk size
        if j == i + int(0.5 * n):
            j = min(i + n, len(tokens))
        yield tokens[i:j]
        i = j


# Define a function to send a question to ChatGPT and receive a response
def summarize(content):
    
    # get the number of tokens
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = create_chunks(content,MAX_TOKENS,tokenizer)
    text_chunks = [ tokenizer.decode(token) for token in tokens ]
    
    # Use the OpenAI API to generate a response to the question   
    for chunk in text_chunks:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages= [
                {"role": "system", "content" : "You are summarizing web pages for a human so they can read it fast"},
                {"role": "user", "content" : "As the best market researcher, summarize the following into a list of key points: " + chunk}
            ]
        )

    # Extract the response text from the OpenAI API response
    print(response.choices[0].message.content)

try: 
    # Command line url
    if len(sys.argv) > 1:
        url = sys.argv[1]
        crawl(url)
    else : 
        # Input  loop
        while True:
            # Get a question from the user and process it
            url = input(">> Enter URL: ")
            # Crawl the website for relevant content
            crawl(url)
except KeyboardInterrupt:
    print("\nUser interrupted process")
# except Exception as e:
#     print("\nAn exception occurred - exiting")

exit()
