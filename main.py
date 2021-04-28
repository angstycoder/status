from flask import render_template
from flask import Flask, request
from os import urandom



message = "Welcome to my website"

# Initialize the app with random secret_key
app = Flask(__name__)
app.secret_key = urandom(12)



@app.route("/")
def index():
    return render_template("index.html", message=message)


@app.route("/change/<msg>")
def change(msg):
    global message
    message = msg
    print(message)
    return render_template("index.html", message=message)


if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=8080, debug=False)
    app.run(debug=False)

