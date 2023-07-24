from flask import Flask,jsonify,request
from image__processing import recognize_celebrities
import os

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    # For a basic health check, we can simply return a JSON response indicating the service is up.
    return jsonify({"status": "healthy"})

@app.route('/clientrequest', methods=['POST'])
def client_request_handler():
    try:
        # Get the data from the client's request (assuming it's in JSON format)
        # data = request.get_json()
        if "image" in request.files:
            file = request.files['image']
            filename = file.filename
            file.save(os.path.join(os.getcwd(), filename))

            # Perform any processing or business logic based on the data from the client
            # For example, you can extract information, call other functions, etc.
            result = process_client_image(filename)
            # Return the result as a JSON response
            return jsonify(result)
        else:
            # Return the result as a JSON response
            return jsonify([])
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def process_client_image(filename):
    # Perform any processing or business logic based on the data from the client
    return recognize_celebrities(filename)
         
    
if __name__ == '__main__':
    app.run()



