from flask import Flask, request, jsonify
import os
import time
from logtail import LogtailHandler
import logging

# Configure logging
handler = LogtailHandler(source_token="thotTjgPgtkWPNVQS9vrcmem")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"Message": "Working"})

@app.route('/delayed-response')
def delayed_response():
    time.sleep(300)  # Sleep for 5 minutes
    return jsonify({"message": "data"})
    
@app.route('/log', methods=['POST'])
def log_request():
    method = request.method
    logger.info(f"Request Method: {method}")
    
    headers = request.headers
    logger.info("Request Headers:")
    for header, value in headers.items():
        logger.info(f"{header}: {value}")

    url = request.url
    logger.info(f"Request URL: {url}")

    args = request.args
    logger.info("Query Parameters:")
    for arg, value in args.items():
        logger.info(f"{arg}: {value}")

    if request.method in ['POST', 'PUT']:
        form_data = request.form
        logger.info("Form Data:")
        for key, value in form_data.items():
            logger.info(f"{key}: {value}")

    body = request.get_data()
    logger.info(f"Request Body: {body}")

    size_in_bytes = len(body)
    logger.info(f"Request Size: {size_in_bytes} bytes")

    return jsonify({"message": "Request logged successfully!"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
