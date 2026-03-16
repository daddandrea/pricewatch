import django
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pricewatch.settings")
django.setup()

from products.scraper import scrape_price
from products.models import Product

product = Product.objects.first()
scrape_price(product)
