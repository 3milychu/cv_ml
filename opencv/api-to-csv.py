import numpy as np
import pandas as pd
import cv2 as cv
from matplotlib import pyplot as plt

df = pd.read_csv('/Volumes/Samsung_T3/project-repos/majorstudio/data/clothes/costume_reclass.csv')
print(df.head())

# Read the 1) image names, 2) image urls, 3) any other info you need:
label = df['img']
url = df['src']

# If pulling from API for below:
number = df['number']
objectID = df['objectID']

# API Request

myJson=[]

import urllib.request
import json
import csv

for i in range(0,1000):
    base_url = 'https://collectionapi.metmuseum.org/api/collection/v1/object/'
    objectid = str(int(objectID[i]))
    url = base_url + objectid
    req = urllib.request.Request(url)

    ##parsing response
    r = urllib.request.urlopen(req).read()
    data = json.loads(r.decode('utf-8'))
    
    ##parsing json
    for objectid in data['location']['gallery']:
        location = data['location']['gallery']
        gallery, gallery_num = location.split()
        gallery_num_int = int(gallery_num)
       
        if gallery_num_int > 755 and gallery_num_int < 772:
            var = {"Title": data['titles']['primaryTitle'],"Gallery": data['location']['gallery'],
                   "Image URL": data['media']['images']['primaryImage']['imageUrl'], 
                   "URL": data['metadata']['metaCanonicalURL']}
            myJson.append(var.copy())

# Create table with list values
import pandas
myJson_df = pandas.DataFrame(myJson)
myJson_table = myJson_df.drop_duplicates(keep='first', inplace=False)
print(myJson_table)

# Write to csv
myJson_table.to_csv("./file.csv", sep=',',index=False)
