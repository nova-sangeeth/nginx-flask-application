<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "This is now working!!!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


    
=======
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == "POST"):
        nova = request.get_json()
        return jsonify({'name': nova}), 201
    else:
        return jsonify({"about": "Hello World"})


@app.route('/api/<int:num>', methods=['GET'])
def get_multiply(num):
    return jsonify({'result': num*10})


if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 1bdefb25433ab1253ad68fc5bd6da176fc3fe680
