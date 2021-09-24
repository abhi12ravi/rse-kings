#!/usr/bin/python3
# Usage: python get_data.py <path_to_output_file>

import requests

API_END_POINT_HELLO = "http://127.0.0.1:5000/helloworld" #Edit this URL as per need

API_ENDPOINT_ECHO = "http://127.0.0.1:5000/echo" #Edit this URL as per need

def main():
    
    #1.Call hello GET request
    print("Fetching response from helloworld end-point...")    
    r = requests.get(url = API_END_POINT_HELLO)
    data = r.text
    print("Data retrived from HelloWorld end-point:", data)
    print("================================================")

    #2.Call echo endpoint POST request
    # data = "Hello, how do you do?"
    # r = requests.post(url = API_ENDPOINT_ECHO, data = data)

    # r = requests.post("http://127.0.0.1:5000/echo/?data='Howdy'")

    # # extracting response text 
    # print(r)



if __name__=='__main__':
   main()
