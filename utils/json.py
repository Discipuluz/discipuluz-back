import os, json
from pprint import pprint

def read(file):
    with open(os.path.join(os.path.dirname(__file__), '../res/datas/' + file + '.json')) as data_file:    
        data = json.load(data_file)

    pprint(data)
    return data