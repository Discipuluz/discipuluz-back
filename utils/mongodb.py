from pymongo import MongoClient
import datetime

def init(api):
    client = MongoClient(api.config['mongodb']['host'])
    api.vars['db'] = client[api.config['mongodb']['database']]

def insert(api, collection, record):
    record['_datetime'] = datetime.datetime.now()
    record['_isRemoved'] = False
    result_id = api.vars['db'][collection].insert(record)
    print result_id
    return result_id

def select(api, collection, by = {}):
    cursor = api.vars['db'][collection].find(by)
    result = []
    for doc in cursor:
        yield doc

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