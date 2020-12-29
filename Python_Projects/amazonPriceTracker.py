"""
  Amazon Product Price Tracker Program
  URL --> Specifies the url of the product (Maango Sitar Branded Stylish Latest Girls college Bags)

 checkPrice() method fetches the  current price of the Product in the specified URL
"""

import requests
from bs4 import BeautifulSoup
URL = 'https://www.amazon.in/Maango-Sitar-Womens-Messenger-Blue/dp/B07PY8YMJP/ref=pd_rhf_eebr_s_pd_crcd_1_3'
myuseragent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'


def checkPrice():
  headers = {"User-Agent": myuseragent}
  page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(page.content,'html.parser')
  price = soup.find(id='priceblock_ourprice').get_text().strip()
  price = float(price[2:])
  return price

print("The Price of product is {0}".format(checkPrice()))