import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging
from urllib.parse import quote

search_query = "Washing Machine"
encoded_query = quote(search_query)
flipkart_url = "https://www.flipkart.com/search?q=" + encoded_query

url_client = urlopen(flipkart_url)
flipkart_page = url_client.read()
flipkart_html = bs(flipkart_page, "html.parser") 
big_box = flipkart_html.find_all("div", {"class":"cPHDOP col-12-12"})
print(len(big_box))
del big_box[0:3]
print(len(big_box))
# for i in big_box:
#     link = i.div.div.div.a
#     if link:  # Check if 'a' tag exists
#         print("https://www.flipkart.com/" + link['href'])
product_link = "https://www.flipkart.com" + big_box[0].div.div.div.a['href']
print(product_link)
product_req = requests.get(product_link)
product_html = bs(product_req.text, 'html.parser')
comments = product_html.find_all('div', {'class':"RcXBOT"})
print(len(comments))
print(comments[0].div.div.find_all("p",{"class":"_2NsDsF AwS1CA"})[0].text)
# for i in comments:
#     print(i.div.div.find_all("p",{"class":"_2NsDsF AwS1CA"})[0].text)
print(comments[0].div.div.div.div.text)
# for i in comments:
#     print(i.div.div.div.div.text)
print(comments[0].div.div.div.p.text)
# for i in comments:
#      print(i.div.div.div.p.text)
print(comments[0].div.div.find_all("div",{"class":""})[0].div.text)
# for i in comments:
#     print(i.div.div.find_all("div",{"class":""})[0].div.text)
