from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    ret = "<h1>Hello, world.</h1>"
    ret += "<h3>This is my environment:</h3>"
    ret += "<table>"
    ret += "<tr><th>Key</th><th>Value</th></tr>"

    for k in os.environ.keys():
        ret += "<tr><td>" + k + "</td><td>" + os.environ[k] + "</td></tr>"

    ret += "</table>"
    return ret

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')