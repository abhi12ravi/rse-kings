#!/usr/bin/python3
# Usage: python get_data.py <path_to_output_file>

from flask import Flask, json

api = Flask(__name__)

@api.route('/helloworld', methods=['GET'])
def say_hello():
    return "helloworld"


if __name__=='__main__':
   api.run()
