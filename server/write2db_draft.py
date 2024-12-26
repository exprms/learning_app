#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:45:57 2024

@author: bernd
"""
# import csv
import json
import requests
import csv


import csv, sqlite3

con = sqlite3.connect('/home/bernd/Projects/learning_app/learning_app.db')
cur = con.cursor()

with open('/home/bernd/Courses/cesky/czech_vocabs.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    to_db = [(row['id'], row['left'], row['right'], row['info_left'], row['info_right']) for row in reader]
    
cur.executemany("INSERT INTO pair (id, left, right, info_left, info_right) VALUES (?, ?, ?, ?, ?);", to_db)
con.commit()


with open('/home/bernd/Courses/cesky/tags.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    to_db = [(row['id'], row['tag']) for row in reader]
    
cur.executemany("INSERT INTO tag (id, tag) VALUES (?, ?);", to_db)
con.commit()


with open('/home/bernd/Courses/cesky/vocabtags.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    to_db = [(row['id'], row['pair_id'], row['tag_id']) for row in reader]
    
cur.executemany("INSERT INTO pairtag (id, pair_id, tag_id) VALUES (?, ?, ?);", to_db)
con.commit()
con.close()

    
# with open(fname, 'r') as csv_file:
#     data = csv.reader(csv_file, delimiter=';')


# fname = '/home/bernd/Projects/learning_app/data/verbs_unit2.csv'

# with open(fname, mode ='r') as file:
#   textFile = file.readlines()
    
# entry_dict = {
#   "id": 9,
#   "topic": "czech",
#   "chapter": "verbs unit 2",
#   "mode": "vocab",
#   "left": "být",
#   "right": "sein"
#   }
# id_counter = 10
# for lines in textFile:
#     left = lines.split(';')[0]
#     right = lines.split(';')[1]
#     right = right.split('\n')[0]
#     entry_dict.update({
#         "id": id_counter,
#         "left": left,
#         "right": right
#         })
#     requests.post(url="http://localhost:8000/pairs/", data=json.dumps(entry_dict))
#     id_counter += 1


