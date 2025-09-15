from flask import Flask

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
def hello_world(path):
    return 'Hello, World!\n', 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=False)