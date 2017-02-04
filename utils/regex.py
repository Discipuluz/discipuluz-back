#!/usr/bin/env python
# coding: utf-8

import re

def match(regex, match_str):
    return re.match(regex, match_str)

def search(regex, match_str):
    return re.search(regex, match_str)