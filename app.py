from flask import Flask
import os, sys

if len(sys.argv) >= 2:
    port = int(sys.argv[1])
else:
    port = 5000

if len(sys.argv) >= 3:
    message = sys.argv[2]
else:
    message = "world"

app = Flask(__name__)

@app.route('/')
def hello_world():
    ret = "<h1>Hello, " + message + "!</h1>"
    ret += "<h3>This is my environment:</h3>"
    ret += "<table>"
    ret += "<tr><th>Key</th><th>Value</th></tr>"

    keys = list(os.environ.keys())
    keys.sort()
    for k in keys:
        ret += "<tr><td>" + k + "</td><td>" + os.environ[k] + "</td></tr>"

    ret += "</table>"
    return ret

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=port)