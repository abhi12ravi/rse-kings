# RSE at King's 
This is a task for the RSE (Research Software Engineer) role at King's College, London.

## Goals of this project
1. To develop a HTTP server in Python as described in the task description

## Task description:
```
"Please develop an HTTP server in a language of your choice. 

The server should have two endpoints, a GET route, available at '/helloworld', that responds with 'helloworld', and a POST route, available at '/echo', that accepts a body of data, and returns that same body of data as a part of the response. 

Please also supply a 'driver' program, which demonstrates the functionality of the server by calling each route. 

Detailed comments should be added to explain the functionality of the code produced." 
```

## Solution
1. `scripts/flask-api.py` - A Flask based HTTP server implementation that includes one GET endpoint and one POST endpoint.
2. `scripts/driver.py` - A driver program that demonstrates the functionality of the server by calling both the routes.


## Steps to run the file
1. Clone the repo to a suitable directory
2. Install the requirements in the `requirements.txt` file 
3. Start a Flask HTTP Server in a shell and keep it running like this:
```
PS C:\Users\Abhi\Documents\rse-kings2> python .\scripts\flask-api.py
 * Serving Flask app 'flask-api' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
5. Copy the local URL and paste in the driver.py file (lines 6 and 8 of `scripts/driver.py` file)
6. In another shell, run the driver program this way: `$python scripts/driver.py`

Output:
```
PS C:\Users\Abhi\Documents\rse-kings2> python .\scripts\driver.py
Fetching response from helloworld end-point...
Data retrived from helloworld end-point: helloworld
=============================================================
Fetching response from echo end-point...
Data retrived from echo end-point:
Sun rises in the east.
=============================================================
```
8. Customizations can be made to the input body of data by changing the variable `input_data_body` on line 21 of `scripts/driver.py` file.

## References
1. [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
2. [3 Lines of Python Code to Write A Web Server](https://towardsdatascience.com/3-lines-of-python-code-to-write-a-web-server-46a109666dbf)
