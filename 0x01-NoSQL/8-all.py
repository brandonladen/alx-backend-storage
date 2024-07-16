#!/usr/bin/env python3
'''8-all'''


def list_all(mongo_collection):
    '''lists all docs in a collection'''

    mydoc = mongo_collection.find()
    if not mydoc:
        return []

    return mongo_collection.find()
