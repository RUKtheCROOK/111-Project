#!usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.get('/aboutme')
def aboutme():
    me = {'first_name': 'John', 'last_name': 'Garcia', 'hobby': 'Gaming'}
    return (me)