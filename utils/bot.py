#!/usr/bin/env python
# coding: utf-8

import aiohttp
import json

async def message(api, user_id, email, text):
    with aiohttp.ClientSession() as session:
        await notify(api, user_id, email, 'dispatched')
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

async def notify(api, user_id, email_from, email_to, event, error={}):
    with aiohttp.ClientSession() as session:
        async with session.post(api.config['bot']['url']['notifications'],
                        data=json.dumps({
                            'id': user_id,
                            'from': email_from,
                            'to': email_to,
                            'event': event,
                            'reason': error
                        }),
                        headers={
                            'Content-Type': 'application/json',
                            'Authorization': 'Key ' + api.config['bot']['token']
                        }) as resp:
            api.debug(resp.status)
            api.debug(await resp.text())
