import os
import requests
from bs4 import BeautifulSoup
# import lxml
import smtplib

URL ="https://www.amazon.fr/dp/B09Z2YLNKM/ref=twister_B08C5KHS9V?_encoding=UTF8&th=1"
amazon_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(URL, headers=amazon_headers)
# print(response.status_code)
web_data = response.content

# if "bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: html-parser" --> use lxml
# soup = BeautifulSoup(web_data, parser=lxml, features="lxml")
soup = BeautifulSoup(web_data, "html.parser")
# print(soup.prettify())

price_tag = soup.select_one("span.a-offscreen")
price = float(price_tag.getText().replace(",", ".").split("€")[0])
print(price)
# print(type(price))

price_wanted = float(input("What price do you want to get? In this format, please: 12.85.\n"))

if price_wanted >= price:
    print("send email")
    MY_EMAIL = os.environ["MY_EMAIL"]
    GMAIL_SERVER = "smtp.gmail.com"
    MY_PASSWORD = os.environ["MY_PASSWORD"]
    EMAIL_TEST = os.environ["EMAIL_TEST"]
    with smtplib.SMTP(GMAIL_SERVER, port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=EMAIL_TEST,
                            msg=f"Subject: It's time to pay!\n\n"
                                f"The price for the item you wanted is equal to or below {price_wanted} €."
                                f"Check it now: {URL}")
