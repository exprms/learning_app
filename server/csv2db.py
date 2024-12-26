#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:45:57 2024

@author: bernd
"""
# import csv
import json
import csv
import sqlite3
from server.constants import (
    DATABASE_FILEPATH, 
    DATABASE_NAME,
    DATA_CSV,
    TABLE_NAME,
    csv_map
    )


con = sqlite3.connect(DATABASE_FILEPATH + DATABASE_NAME)
cur = con.cursor()

with open(DATA_CSV, newline='') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=csv_map.source_column_names, delimiter=';')
    # create tuples:
    data_to_db = []
    for row in reader:
        # dumps tag columns into list
        tag_col = json.dumps({csv_map.json_columns.name: [row[item] for item in csv_map.json_columns.columns if row[item] != ""]})
        
        # normal columns:
        data_row = [row[item] for item in csv_map.columns]
        
        # append together
        data_row.append(tag_col)
        data_to_db.append(tuple(data_row))
        
print(data_to_db[0])      
number_table_columns = len(csv_map.columns) + 1
column_name_string = '(' + ','.join(csv_map.target_column_names) + ')'
value_string = '(' + ','.join(['?' for k in range(number_table_columns)]) + ')'        
insert_string = f"INSERT INTO {TABLE_NAME} {column_name_string} VALUES {value_string};"
print(insert_string)
cur.executemany(insert_string, data_to_db)
con.commit()
con.close()

# SQL STRING FOR UNIQUE TAGS:
# select 
#   distinct json_each.value 
# from pair, json_each(json_extract(pair.tags, '$.tags'));

# filter query:
# select 
#   distinct pair.left, 
#   json_each.value as tags 
# from pair, json_each(json_extract(pair.tags, '$.tags')) 
# where json_each.value = 'Verb';
