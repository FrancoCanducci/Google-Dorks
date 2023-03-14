from googlesearch import search

# Define the Google Dork query
query = "site:example.com intitle:index.of"

# Perform the search and print the results
for url in search(query, num_results=10):
    print(url)