#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pypolyback import async

utils = [
    'mysql',
    'mongodb',
    'json'
]

def get(req, api):
    """
    Start the server
    Then go, from your browser, in `localhost:8888/example/ex_endpoint`
    There shoud open a page with the content `Success in method get!`

    Output:
        string
    """
    result = api.json.read('test')
    
    req.send({
        'resultados': str(result)
    }) #retornando os dados

def post(req, api):
    """
    Start the server
    Then make a post http request to `localhost:8888/example/ex_endpoint`
    Sending the documented object as input 
    It should be returned `{"message": input.message, "status":"Sucess in method post!"}`

    Input:
        message: string

    Output:
        message: string
        request: string
    """

    message = req.params['message'] #coletando dados da requisição

    #retornando os dados
    req.send({
        'message': api.example_util.write(req),
        'request': message
    })