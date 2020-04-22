from bs4 import BeautifulSoup as bs
import requests
from links import get_links

filename = 'timesofindia_tweets.csv'
targets = get_links(filename)

'''
format for data:
{
'source' : 'times_of_india',
'title' : "",
'paragraphs':[""],
'publication':"<timestamp>",
'category':"",
'tags':""
}
'''
for target in targets:
  row = {
    'source' : 'times_of_india',
    'title' : "",
    'paragraphs':[""],
    'publication':"",
    'category':"",
    'tags':""
  }
  row['publication'] = target['datetime']
  req = requests.get(target['link'])
  soup = bs(req.text, 'html.parser')
  heading = soup.find_all('h1')
  for i in heading:
    # ignore links for other tweets
    if i.find(class_='ProfileHeaderCard-nameLink'):
      continue
    
    # if ToI link
    elif (i.find('arttitle') != None):
      row['title'] = (i.find('arttitle').text)
      print(row['title'])
    
    else:
      row['title'] = (i.text)
      print(row['title'])
  # print(row['title'])
  
    
    