#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import logging

from flask import Flask
from random import randint

logger = logging.getLogger(__name__)
hdlr = logging.FileHandler('/deploy/app/main.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

app = Flask(__name__)

MSGS = [
    "Hello there",
    "How are you?",
    "Hey!"
]

@app.route("/")
def hello():
    return get_fun_msg()


def get_fun_msg():
    return MSGS[randint(0, len(MSGS)-1)]


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 8000.
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)