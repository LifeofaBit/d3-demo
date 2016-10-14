# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 09:40:39 2016

@author: mdowns
"""

import csv

with open('../data/spawn_rate.csv', 'rU') as infile, open('../data/mon_rate_chart.tsv', 'w') as outfile:
    reader = csv.reader(infile)    
    writer = csv.writer(outfile, delimiter='\t')
    
    writer.writerow(['id', 'name', 'rate', 'type'])
    writer.writerows(row[0:2] + row[3:] for row in reader)