from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['POST'])
def process_data():
    data = request.json
    # Process the data here
    response = {'message': 'Data received', 'data': data}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
