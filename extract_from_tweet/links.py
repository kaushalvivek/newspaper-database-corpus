import csv

def get_links(filename):
  data_points = []
  with open('Tweets/'+filename, 'r') as f:
    data = csv.reader(f)
    for row in data:
      text = row[2]
      words = text.split()
      for i in words:
        data_point={
          'link':"",
          'datetime':""
        }
        if(i.startswith('https://t.co/')):
          data_point['link']=(i.strip('\'').strip('\"'))
          data_point['datetime']=row[1]
          data_points.append(data_point)
  return data_points