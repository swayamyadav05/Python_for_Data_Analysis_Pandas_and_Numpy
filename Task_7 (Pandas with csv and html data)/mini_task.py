# Pandas is used to read a csv file and store data in a DataFrame
from urllib import request
import ssl
import pandas as pd

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.livingin-canada.com/house-prices-canada.html"
html = request.urlopen(url, context=ctx).read()

# house_price_df = pd.read_html('https://www.livingin-canada.com/house-prices-canada.html', context = ctx)
house_price_df = pd.read_html(html)
print(house_price_df[0])
print("-" * 80)
print(house_price_df[1])
print("-" * 80)


"""
MINI CHALLENGE #7:

Write a code that uses Pandas to read tabular US retirement data
You can use data from here: https://www.ssa.gov/oact/progdata/nra.html
"""

from urllib import request
import ssl
import pandas as pd

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.ssa.gov/oact/progdata/nra.html"
html = request.urlopen(url, context=ctx).read()

# house_price_df = pd.read_html('https://www.livingin-canada.com/house-prices-canada.html', context = ctx)
# house_price_df[0]
# house_price_df[1]

retirement_df = pd.read_html(html)
print(retirement_df[0])
print("-" * 80)
