#!/usr/bin/env python
# coding: utf-8

import aiohttp
import json

async def message(api, user_id, email, text):
    with aiohttp.ClientSession() as session:
        notify(api, user_id, email, 'dispatched')
        async with session.post(api.config['bot']['url']['messages'],
                        data=json.dumps({
                            'id': user_id,
                            'to': email,
                            'type': 'text/plain',
                            'content': text
                        }),
                        headers={
                            'Content-Type': 'application/json',
                            'Authorization': 'Key ' + api.config['bot']['token']
                        }) as resp:
            api.debug(resp.status)
            api.debug(await resp.text())

async def notify(api, user_id, email, event, error={}):
    with aiohttp.ClientSession() as session:
        async with session.post(api.config['bot']['url']['messages'],
                        data=json.dumps({
                            'id': user_id,
                            'from': email,
                            'content': event,
                            'reason': error
                        }),
                        headers={
                            'Content-Type': 'application/json',
                            'Authorization': 'Key ' + api.config['bot']['token']
                        }) as resp:
            api.debug(resp.status)
            api.debug(await resp.text())
