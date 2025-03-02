from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize a variable to store the health data
health_data = {}

# Endpoint to send the health data to the frontend
@app.route('/get-health-data', methods=['GET'])
def get_health_data():
    try:
        # Send the health data as JSON
        return jsonify(health_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/health-data', methods=['POST'])
def receive_data():
    data = request.get_json()
    
    # Check if the required keys are in the received JSON data
    if 'heartRate' not in data or 'SpO2' not in data or 'temperature' not in data:
        return jsonify({"error": "Missing required health data"}), 400
    
    heart_rate = data['heartRate']
    spO2 = data['SpO2']
    temperature = data['temperature']
    
    # Store the received data into the health_data variable
    health_data['heartRate'] = heart_rate
    health_data['SpO2'] = spO2
    health_data['temperature'] = temperature
    
    print(f"Received data - Heart Rate: {heart_rate}, SpO2: {spO2}, Temperature: {temperature}")
    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
