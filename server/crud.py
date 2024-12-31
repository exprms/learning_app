# -*- coding: utf-8 -*-
import json
from sqlalchemy.orm import Session
from sqlalchemy import text

import server.schemas as schemas
from server.constants import TABLE_NAME, csv_map, TAG_VIEW

pair_col = csv_map.target_column_names

def pair_mapper(cols: list[str], item_: tuple) -> dict:
    out_dict = {}
    for index, col in enumerate(cols):
        if col == csv_map.json_columns.name:
            tmp = json.loads(item_[index])[csv_map.json_columns.name]
            out_dict.update({col: tmp})
        else:
            out_dict.update({col: item_[index]})
         
    return out_dict

def query_maker(q_type, where_clause = "", tag_list = []) -> str:
    pair_col = csv_map.target_column_names
    if q_type == 'pair_by_where':
        return f"SELECT {','.join(pair_col)} FROM {TABLE_NAME} {where_clause}"
      
    elif (q_type == 'pair_by_tags'):
        sql_str = []
        for item in tag_list:
            tmp = f"SELECT distinct {TABLE_NAME}.* " 
            tmp += f" FROM {TABLE_NAME}, json_each(json_extract({TABLE_NAME}.{csv_map.json_columns.name}, '$.{csv_map.json_columns.name}')) " 
            tmp += f" WHERE json_each.value = '{item}'"
            sql_str.append(tmp)
        return " INTERSECT ".join(sql_str)
    
    pass
    
def get_pair(db: Session, sql_stmt: str = f"select * from {TABLE_NAME}") -> list[schemas.Pair]:    
    stmt = text(sql_stmt)
    result = db.execute(stmt).fetchall()
    return [schemas.Pair(**pair_mapper(cols=pair_col, item_=row)) for row in result]

def get_tags(db: Session) -> list[str]:
    stmt = text(f"SELECT * FROM {TAG_VIEW}")
    result = db.execute(stmt).fetchall()
    return [item[0] for item in result]
    

