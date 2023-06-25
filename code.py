#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pymongo')
import pymongo
from pymongo import MongoClient
mytree=ET.parse(r'D:\\Fourth Semester\\BDA\\dblp.xml')
root=mytree.getroot()
print(root)
import xml.etree.ElementTree as ET
client =pymongo.MongoClient()
db= client['i20-1853']
collection=db['DBLP_DATA']
d = {}
for i in root:
        d["type"]=i.tag
        for x in i:
            d[x.tag]=x.text
        collection.insert_one(d)
        d={}

