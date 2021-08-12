'''from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    """ """

    return "This is OK."


@app.route("/route1", methods=["GET"])
def my_get_method():
    """
    GET method
    """

    response = {
        "Status": "200 OK",
        "Method": request.method,
    }
    return jsonify(response)


@app.route("/route2", methods=["POST"])
def my_post_method():
    """
    POST Method
    """
    req = request.get_json()
    response = jsonify(req)
    return response


@app.route("/route3", methods=["GET"])
def route3():
    """
    GET Method
    """
    key = "user"
    searchword = request.args.get(key, "")
    d = {
        "Status": "200 OK",
        "Method": request.method,
        "Data": {
            key: searchword,
        },
    }
    response = jsonify(d)
    return response


@app.route("/route4/<name>", methods=["PUT"])
def route4(name):
    """
    PUT Method
    """
    # do whatever you want with the argument 'name'
    # ..
    d = {
        "Status": "200 OK",
        "Method": request.method,
        "Data": {
            "name": name,
        },
    }
    response = jsonify(d)
    return response


if __name__ == "__main__":
    app.run()
'''
