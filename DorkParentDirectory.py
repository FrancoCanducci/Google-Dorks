import os
import requests
from bs4 import BeautifulSoup
from googlesearch import search

# Define the Google Dork query
query = 'intitle:index.of "parent directory" "name" "size" "modified" "description"'

# Perform the search and download matching files
for url in search(query, stop=10):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href.endswith('.mp4') or href.endswith('.pdf'):
                file_url = url + '/' + href
                file_path = os.path.join(os.getcwd(), href)
                with open(file_path, 'wb') as file:
                    response = requests.get(file_url)
                    file.write(response.content)
                print(f'Downloaded {href} from {url}')
    except:
        print(f'Error downloading files from {url}')