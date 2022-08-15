import requests
from bs4 import BeautifulSoup
url = "https://habr.com/ru/all/"
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")
all_links = soup.find_all("a", class_="tm-article-snippet__title-link")
for link in all_links:
    print("https://habr.com" + link["href"])