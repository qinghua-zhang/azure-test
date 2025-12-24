from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "hello world"})

@app.route('/api')
def api_hello():
    return jsonify({"message": "hello world"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

