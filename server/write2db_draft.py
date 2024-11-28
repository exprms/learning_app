#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:45:57 2024

@author: bernd
"""
# import csv
import json
import requests

fname = '/home/bernd/Projects/learning_app/data/verbs_unit2.csv'

with open(fname, mode ='r') as file:
  textFile = file.readlines()
    
entry_dict = {
  "id": 9,
  "topic": "czech",
  "chapter": "verbs unit 2",
  "mode": "vocab",
  "left": "být",
  "right": "sein"
  }
id_counter = 10
for lines in textFile:
    left = lines.split(';')[0]
    right = lines.split(';')[1]
    right = right.split('\n')[0]
    entry_dict.update({
        "id": id_counter,
        "left": left,
        "right": right
        })
    requests.post(url="http://localhost:8000/pairs/", data=json.dumps(entry_dict))
    id_counter += 1
