from flask import Flask, request, jsonify

# The below creates a flask object;this is used to set up all of our different routes(i.e.http requests)
app: Flask = Flask(__name__)
# app: Flask = Flask()


@app.route("/greeting", methods=["GET"])
def hello_world():
    return "Hello World"


app.run()
