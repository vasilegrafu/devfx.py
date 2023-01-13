import flask as fk
import datetime as dt

app = fk.Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask!' + ' ' + dt.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%fZ')

if __name__ == '__main__':
    app.run(debug=True)