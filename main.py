#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from random import randint

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
