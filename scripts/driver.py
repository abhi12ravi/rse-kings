#!/usr/bin/python3
# Usage: python get_data.py <path_to_output_file>

import requests

API_END_POINT_HELLO = "http://127.0.0.1:5000/helloworld" #Edit this URL as per need

API_ENDPOINT_ECHO = "http://127.0.0.1:5000/echo?data=" #Edit this URL as per need

def main():
    
    #1.Call helloworld GET request
    print("Fetching response from helloworld end-point...")    
    r = requests.get(url = API_END_POINT_HELLO)
    data = r.text
    print("Data retrived from helloworld end-point:", data)
    print("=============================================================")

    #2.Call echo endpoint POST request
    print("Fetching response from echo end-point...")  
    input_data_body = "Sun rises in the east." #Change this input text body as per need.
    URL = API_ENDPOINT_ECHO + input_data_body
    r = requests.post(URL)
    print("Data retrived from echo end-point:")
    print(r.text)
    print("=============================================================")

if __name__=='__main__':
   main()
