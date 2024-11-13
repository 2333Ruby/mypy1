from bs4 import BeautifulSoup
import requests
content = requests.get("http://books.toscrape.com/").text
soup = BeautifulSoup(content,"html.parser")
all_prices = soup.findAll("p",attrs={"class":"price_color"})
for price in all_prices:
    print(price)