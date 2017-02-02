#!/usr/bin/env python
# coding: utf-8

import cyclone.mail
import cyclone.web

me = None

def init(api):
    me = api.config['mail']['username']

def any(req, api):
    req.to = req.params['email']

def send(req, subject, message=''):
    msg = cyclone.mail.Message(
            from_addr=me,
            to_addrs=req.to,
            subject=subject,
            message=message,
            mime='html',  # optional. default=text/plain
            charset="utf-8")    # optional. default=utf-8

    try:
        response = yield cyclone.mail.sendmail(req.settings.email_settings, msg)
        return True
    except Exception, e:
        return False
