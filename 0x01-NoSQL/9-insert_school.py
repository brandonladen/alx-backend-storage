#!/usr/bin/env python3
'''9-insert_school'''


def insert_school(mongo_collection, **kwargs):
    '''inserts a new doc in a collection and returns id'''
    result_id = mongo_collection.insert(kwargs)
    return result_id
