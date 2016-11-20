import json
from pprint import pprint

def post(req, api):
    with open('res/datas/holland.json') as data_file:    
        data = json.load(data_file)
        return data 