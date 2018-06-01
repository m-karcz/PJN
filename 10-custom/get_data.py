import requests
import pickle
import json

appkey = "" #here was appkey
url = "http://a.wykop.pl/links/promoted/appkey,{}/page,{}/"

print(url)

data = []

for page in range(1, 200):
    req = requests.get(url.format(appkey, page))
    res = json.loads(req.text)
    data.extend(res)

with open("rawdata.pickle", "wb") as fp:
    pickle.dump(data, fp)
