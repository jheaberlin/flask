from flask import Flask, request, jsonify
import random
import string

# Configure logging
handler = LogtailHandler(source_token="thotTjgPgtkWPNVQS9vrcmem")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

app = Flask(__name__)

keys = [f"key_{i}" for i in range(1, 301)]

def generate_random_value():
    """Generate a random value consisting of alphanumeric characters."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def generate_object():
    """Generate a single object with 300 key-value pairs."""
    return {key: generate_random_value() for key in keys}

@app.route('/generate', methods=['GET'])
def generate_objects():
    try:
        # Number of objects to return, default is 1
        num_objects = int(request.args.get('num', 1))
        
        if num_objects < 1:
            return jsonify({"error": "Number of objects must be at least 1"}), 400
        
        # Generate the list of objects
        data = [generate_object() for _ in range(num_objects)]
        
        return jsonify(data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
