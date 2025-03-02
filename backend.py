from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to handle cross-origin requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Endpoint to handle POST requests with health data
@app.route('/health-data', methods=['POST'])
def handle_health_data():
    # Check if the request contains JSON data
    if request.is_json:
        try:
            # Get the JSON data from the request
            data = request.get_json()

            # Extract the values from the JSON data
            heart_rate = data.get("heart_rate")
            temperature = data.get("temperature")
            spo2 = data.get("spo2")

            # Print the data to the console (for debugging purposes)
            print(f"Heart Rate: {heart_rate} BPM")
            print(f"Temperature: {temperature} °C")
            print(f"SpO2: {spo2} %")

            # Return the received data in the response (in JSON format)
            return jsonify({
                "heart_rate": heart_rate,
                "temperature": temperature,
                "spo2": spo2
            }), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        return jsonify({"error": "Request must be in JSON format"}), 400
    
if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
