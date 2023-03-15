import os
import requests
from bs4 import BeautifulSoup
import lxml

URL ="https://www.amazon.fr/dp/B09Z2YLNKM/ref=twister_B08C5KHS9V?_encoding=UTF8&th=1"
amazon_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(URL, headers=amazon_headers)
# print(response.status_code)
web_data = response.content

# if "bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: html-parser" --> use lxml
soup = BeautifulSoup(web_data, "lxml")
print(soup.prettify())