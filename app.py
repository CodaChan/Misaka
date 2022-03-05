# Copyright 2021 CodaChan
# Completed on Mar 4, 2022

from flask import Flask
from flask import request
from parser_block import Parser

app = Flask(__name__)

@app.route("/misaka")
def api():
    str = request.args.get('str', '')
    return Parser(str)