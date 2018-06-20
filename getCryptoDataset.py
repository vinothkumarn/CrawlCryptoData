import urllib, json
from cryptocmd import CmcScraper
url = "https://min-api.cryptocompare.com/data/all/coinlist"
response = urllib.urlopen(url)
data = json.loads(response.read())
finalCSV = {}
for key,value in data['Data'].items():
  try:
    scraper = CmcScraper(value['Name'])
    headers, data = scraper.get_data()
    finalCSV[value['Name']] = data
  except Exception as e:
    continue
  with open('cryptodataset.json', 'w') as f:
    jsonfile = json.dumps(finalCSV)
    f.write(jsonfile)
  print finalCSV[value['Name']]
f.close()