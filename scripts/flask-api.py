#!/usr/bin/python3
# Usage: python get_data.py <path_to_output_file>

from flask import Flask, request

#Instanstiating Flask
api = Flask(__name__)

#Define GET route
@api.route('/helloworld', methods=['GET'])
def say_hello():
    return "helloworld"

#Define POST route
@api.route('/echo', methods=['POST'])
def echo():
    data = request.args.get('data')
    return(data)

if __name__=='__main__':
   api.run()
