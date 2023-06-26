from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__, static_folder='../frontend', static_url_path='/frontend')

# Configure logging
logging.basicConfig(filename='transaction.log', level=logging.INFO)

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    problem = data.get('problem')

    # Log the transaction
    logging.info(f"Calculation requested for problem: {problem}")

    # Send the arithmetic problem to the backend service
    response = requests.post('http://localhost:8000/calculate', json={'problem': problem})
    result = response.json().get('result')
    error = response.json().get('error')

    # Log the transaction result
    logging.info(f"Calculation result: {result}")

    return jsonify(result=result, error=error)

if __name__ == '__main__':
    app.run()