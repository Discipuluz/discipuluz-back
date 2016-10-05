#!/usr/bin/env python
# coding: utf-8
import os, json, codecs
from pprint import pprint

def read(file):
    with codecs.open(os.path.join(os.path.dirname(__file__), '../res/datas/' + file + '.json'), 'r', 'utf-8-sig') as data_file:
        data_str = data_file.read()
        data = json.loads(data_str)
    return data