from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(message='Hello from the microservice!', timestamp=datetime.datetime.now().isoformat())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
