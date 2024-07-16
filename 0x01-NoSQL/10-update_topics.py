#!/usr/bin/env python3
'''10-update_topics'''


def update_topics(mongo_collection, name, topics):
    '''changes all topics of a school document based on the name'''
    new_vals = {"$set": {"topics": topics}}
    myquery = {"name": name}
    mongo_collection.update_many(myquery, new_vals)
