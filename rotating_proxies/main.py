import requests

with open('valid_proxies.txt', 'r') as f:
    valid_proxies = f.read().splitlines()

sites_to_check = ["http://books.toscrape.com/", 
                  "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html",
                  "http://books.toscrape.com/catalogue/category/books/history_32/index.html"]

count = 0

for site in sites_to_check:
    try:
        print(f"Using proxy {valid_proxies[count]} for {site}")
        response = requests.get(site, proxies={"http": valid_proxies[count], 
                                               "https": valid_proxies[count]})
        print(f"Response code: {response.status_code}")
    except Exception as e:
        print(f"Failed to access {site} using proxy {valid_proxies[count]}: {e}")
    finally:
        count = (count + 1) % len(valid_proxies) # if I have less proxies than sites