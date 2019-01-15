import json
import unicodedata
import ast
from datetime import datetime
from pprint import pprint
import pickle
json_data = []
count = 0
f5 = open('/Users/Pranav/Desktop/UB Sem 1/Information retrieval/Tweets/Topic/politics_tweets-17055.json')
dic={}
dic = json.loads(f5.read())
print(type(dic[0]))
for i in dic:
    i["topic"] = "Politics"
fp = json.dumps(dic)
with open('/Users/Pranav/Desktop/UB Sem 1/Information retrieval/Tweets/Topic/politics_tweets-17055.json', 'w+') as the_file:
  the_file.write(fp)