#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 17:53:00 2024

@author: bernd
"""

from server.schemas import CSVFileMapper, FieldMapper

DATABASE_FILEPATH = '/home/bernd/Projects/learning_app/'
DATABASE_NAME = 'app_db.db'
DATA_CSV = '/home/bernd/Courses/cesky/czech_vocabs_wide.csv'
TABLE_NAME = 'pair'
TAG_VIEW = 'view_tags'

csv_map = CSVFileMapper(
    name=DATA_CSV,
    columns=['id', 'left', 'right', 'info_left', 'info_right', 'tag_subject'],
    json_columns=FieldMapper(
        name='tags',
        columns=[
            'tag_info', 
            'tag_src', 
            'tag_type', 
            'tag_1', 
            'tag_2', 
            'tag_3', 
            'tag_4', 
            'tag_5'
            ]
        )
    )
