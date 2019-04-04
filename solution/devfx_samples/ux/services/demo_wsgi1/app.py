import time
from flask import Flask
app = Flask(__name__)

i = 0

@app.route("/")
def hello_world():
	try:
		global i
		i = i + 1
		return 'Demo_WSGI1: Hello World! ' + str(i)
	except Exception as e:
		return str(e)
		
		
@app.route("/method1")
def hello_world1():
    return 'Hello World 1!'
	
@app.route("/method2")
def hello_world2():
    return 'Hello World 2!'

	
if __name__ == '__main__':
    app.run(debug=True)

	
	