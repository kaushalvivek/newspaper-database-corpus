import csv

def get_links(filename):
  links = []
  with open('Tweets/'+filename, 'r') as f:
    data = csv.reader(f)
    for row in data:
      text = row[2]
      words = text.split()
      for i in words:
        if(i.startswith('https://t.co/')):
          links.append(i.strip('\'').strip('\"'))
  return links