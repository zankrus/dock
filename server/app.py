from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/hithere')
def hi_there_everyone():
    return 'I just here'


@app.route('/buy')
def buy():
    ret_json = {
        'Name': "Dine",
        "age": 22,
        "phones": [
            {
                "phone_type": "iphone8",
                "number": 124565999
            },
            {
                "phone_type": "nokia",
                "number": 12778999
            }
        ]
    }
    return jsonify(ret_json)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
