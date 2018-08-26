from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello World!'
	
@app.route("/method1")
def hello_world1():
    return 'Hello World 1!'
	
@app.route("/method2")
def hello_world2():
    return 'Hello World 2!'
	
if __name__ == '__main__':
    app.run(debug=True)
