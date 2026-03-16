import httpx
from bs4 import BeautifulSoup

from products.models import Product

def scrape_price(product: Product):
    r = httpx.get(product.url)
    soup = BeautifulSoup(r.text, "html.parser")
    print(soup.prettify())
