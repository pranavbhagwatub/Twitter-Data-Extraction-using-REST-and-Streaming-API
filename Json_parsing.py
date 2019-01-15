import json
import unicodedata
import ast
from datetime import datetime
from pprint import pprint
import pickle
json_data = []
count = 0
f6 = open('/Users/Pranav/Desktop/UB Sem 1/Information retrieval/Tweets/Topic/temp.json','w')
f5 = open('/Users/Pranav/Desktop/UB Sem 1/Information retrieval/Tweets/Topic/politics_tweets-17055.json')
for line in f5:
    count = count+1
    line = line.replace('color":"','color":"#' )
    f6.write(line)
f5.close()
f6.close()
f2 = open('/Users/Pranav/Desktop/UB Sem 1/Information retrieval/Tweets/Topic/politics_tweets-17055.json', 'w')
f2.write('[')
counter = 0
with open('/Users/Pranav/Desktop/UB Sem 1/Information retrieval/Tweets/Topic/temp.json') as f:
    for line in f:
        counter = counter + 1
        if line[0] == '{':
            f2.write(line)
            if counter!=count:
                f2.write(',')
                f2.write('\n')
f2.write(']')
f2.close()