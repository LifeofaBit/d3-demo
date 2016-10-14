# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 09:25:35 2016

@author: mdowns
"""

import json, csv

data = []
with open('../data/spawn_rate.csv', 'rU') as infile:
    reader = csv.DictReader(infile, ('id', 'name', 'raw_count', 'spawn_rate', 'type'))
    for row in reader:
        data.append(row)

# Remove header row        
data = data[1:]

temp = {}
for d in data:
    prepared = {
        'name': d['name'],
        'size': int(d['raw_count']),
        'rate': float(d['spawn_rate']),
        'id': int(d['id'])    
    }
    if temp.get(d['type']):
        temp[d['type']].append(prepared)
    else:
        temp.update({d['type']: [prepared]})
  
children = []
for k, v in temp.items():
    children.append({'name': k, 'children': v})
      
final = {'name': 'pokemon', 'children': children}

with open('../data/mon_treemap.json', 'w') as outfile:
    json.dump(final, outfile)


