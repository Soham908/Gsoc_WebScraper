
import pandas as pd
import json
import requests
from urllib.request import urlopen

# url = "https://api.gsocorganizations.dev/organizations.json"
# result = urlopen(url)
#
# data = json.loads(result.read())

with open('gsoc_all_org.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

d = len((data))

#print(d)

name = []
desc = []
topic = []
tech = []
print(d)
e = data[2]['years']
print(type(e))
print(e["2020"])

# for j in range(d):
#     name.append(data[j]['name'])
#     desc.append(data[j][])
#     topic.append(data[j])
#     tech.append(data['organizations'][j]['technologies'])


# dataframe = pd.DataFrame(name)
# dataframe['description'] = desc
# dataframe['topic'] = topic
# dataframe['tech'] = tech
# dataframe.to_csv("comp_all.csv", index=False)

# dataframe = pd.read_csv("comp.csv")

