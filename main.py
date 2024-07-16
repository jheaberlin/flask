from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"Message": "Working"})

@app.route('/log', methods=['POST'])
def log_request():
    method = request.method
    print(f"Request Method: {method}")
    
    headers = request.headers
    print("Request Headers:")
    for header, value in headers.items():
        print(f"{header}: {value}")

    url = request.url
    print(f"Request URL: {url}")

    args = request.args
    print("Query Parameters:")
    for arg, value in args.items():
        print(f"{arg}: {value}")

    if request.method in ['POST', 'PUT']:
        form_data = request.form
        print("Form Data:")
        for key, value in form_data.items():
            print(f"{key}: {value}")

    body = request.get_data()
    print(f"Request Body: {body}")

    size_in_bytes = len(body)
    print(f"Request Size: {size_in_bytes} bytes")

    return jsonify({"message": "Request logged successfully!"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
