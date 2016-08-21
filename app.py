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
    ret = "<html>\n"
    ret += "<body>\n"
    ret += "  <h1>Hello, " + message + "!</h1>\n"
    ret += "  <h3>This is my environment:</h3>\n"
    ret += "  <table>\n"
    ret += "    <tr><th>Key</th><th>Value</th></tr>\n"

    keys = list(os.environ.keys())
    keys.sort()
    for k in keys:
        ret += "    <tr><td>" + k + "</td><td>" + os.environ[k] + "</td></tr>\n"

    ret += "  </table>\n"
    ret += "</body>\n"
    ret += "</html>\n"
    return ret

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=port)