from bs4 import BeautifulSoup
from lab_selectors import extract_listings

with open('sample_merchandise.html', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')

#print(extract_listings(html))

for product in extract_listings(html):
    for i, j in product.items():
        if i == 'name':
            print(j)

#.item
#.badge
#.free-shipping
#.sponsored
##results > li
#.item + .item
#li.item > a