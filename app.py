from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response":"Hola Mundo"})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True) 