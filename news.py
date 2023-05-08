import sys
from googlesearch import search
from datetime import datetime, timedelta
from urllib.parse import urlparse, urlunparse, parse_qs

MAX_RESULTS=5

def clean_url(url):
    parsed_url = urlparse(url)
    cleaned_query = "&".join([f"{k}={v[0]}" for k, v in parse_qs(parsed_url.query).items()])
    cleaned_url = urlunparse(parsed_url._replace(query=cleaned_query))
    return cleaned_url

def print_news_links(query, days=30):
    # Customize the search query to fetch news in the last 30 days
    query = f"{query} when:{days}d"

    for url in search(query, num_results=MAX_RESULTS, lang='en'):
        cleaned_url = clean_url(url)
        print(cleaned_url)

try: 
    # Optional command line subject and days arguments
    if len(sys.argv) > 1: 
        subject = sys.argv[1]        
        days = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        print_news_links(subject, days)

    else : 
        # Input  loop
        while True:
            # Get a question from the user and process it
            subject = input(">> Enter the news subject: ")
            print_news_links(subject)
            
except KeyboardInterrupt:
    print("\nUser interrupted process")
# except Exception as e:
#     print("\nAn exception occurred - exiting")

exit()