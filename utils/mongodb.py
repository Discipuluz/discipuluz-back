from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

def init(api):
    client = MongoClient(api.config['mongodb']['host'])
    api.vars['db'] = client[api.config['mongodb']['database']]

def insert(api, collection, record):
    record['_datetime'] = datetime.datetime.now()
    record['_isRemoved'] = False
    result_id = api.vars['db'][collection].insert(record)
    return result_id

def select(api, collection, by={}, col=[]):
    cursor = api.vars['db'][collection].find(by)
    result = []
    for doc in cursor:
        el = filter(lambda x: x in col, doc)

        # formating ObjectId(_id) to str(id)
        if '_id' in el:
            el['id'] = str(el['_id'])
            del el['_id']

        result += [el]

    return result

def update(api, collection, where, update):
    result = api.vars['db'][collection].update_many(where, {
        '$set': update
    })
    return result.modified_count

def remove(api, collection, where):
    result = update(api, collection, where, {
            'isRemoved': True
        })
    return result

def toObjectId(id):
    return ObjectId(id)
