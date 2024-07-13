# Weather Forecasting API with Flask

This is a Flask-based API designed to provide weather forecasts using a pre-trained LSTM model. The API accepts POST requests with feature data and returns the model's prediction.

## Requirements

- Flask
- TensorFlow
- NumPy

## How It Works

1. **Model Loading**: The API loads a pre-trained LSTM model (`weather_forecasting.h5`) using TensorFlow's `load_model` function.

2. **Input Shape Configuration**:
   - `n_timesteps`: Number of time steps in the sequence (set to 1 for single timestep prediction).
   - `n_features`: Number of features used in the model (set to 6).

3. **Prediction Endpoint**:
   - **Route**: `/predict`
   - **Method**: POST
   - **Request Data**: JSON containing feature data.
     ```json
     {
       "features": [[feature1, feature2, feature3, feature4, feature5, feature6]]
     }
     ```
   - **Response**: JSON containing the prediction.
     ```json
     {
       "prediction": predicted_value
     }
     ```

4. **Error Handling**:
   - If the number of features in the request does not match the expected `n_features`, the API returns a 400 error with a message indicating the issue.

## Running the API

To run the API, execute the script. The Flask application will start and listen for incoming requests on `localhost` with the default port `5000`.

```bash
python app.py
```

Replace `app.py` with the name of your script if it's different.

## Example Usage

To get a prediction, send a POST request to `/predict` with the following JSON body:

```json
{
  "features": [[12.34, 56.78, 90.12, 34.56, 78.90, 12.34]]
}
```

The API will return a JSON response with the forecasted value.

## Error Responses

- **400 Bad Request**: If the number of features does not match the model's expected input.
  ```json
  {
    "error": "Incorrect number of features"
  }
  ```

This API is useful for integrating weather forecasting capabilities into applications that require real-time predictions based on input features.
```
