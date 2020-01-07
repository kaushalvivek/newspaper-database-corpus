'''
The following datapoints for all news articles published in 2019:
- Headline
- Date
- Content
- Category

'''

from bs4 import BeautifulSoup as bs
import requests

years = ['2019']

url = "https://timesofindia.indiatimes.com/archive.cms"

page = requests.get('https://timesofindia.indiatimes.com/archive.cms')
soup = bs(page.text, 'html.parser')
print(soup.prettify)

