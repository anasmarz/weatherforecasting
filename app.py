from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

# Load the model
model = load_model('weather_forecasting.h5')



# Define input shape for the LSTM model
# Adjust these values based on your specific model's configuration
n_timesteps = 1  # Number of time steps in your sequence (e.g., 1 for single timestep prediction)
n_features = 6   # Number of features (e.g., the number of input features used in the model)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json(force=True)
    
    # Extract features and convert to numpy array
    features = np.array(data['features'])
    
    # Check if features length matches the expected number of features
    if features.shape[1] != n_features:
        return jsonify({'error': 'Incorrect number of features'}), 400
    
    # Reshape the input data for the LSTM model
    features = features.reshape((1, n_timesteps, n_features))
    
    # Make prediction
    prediction = model.predict(features)
    
    # Return the prediction as JSON
    return jsonify({'prediction': float(prediction[0][0])})

if __name__ == '__main__':
    app.run(debug=True)
