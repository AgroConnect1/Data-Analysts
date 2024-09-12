from fastapi import FastAPI, Query
from typing import List
import pickle
import numpy as np

# Load the model
model_path = './model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = FastAPI()

@app.get("/predict")
def predict(numbers: List[float] = Query(..., description="List of 7 numbers")):
    if len(numbers) != 7:
        return {"error": "Exactly 7 numbers are required"}

    # Convert input data to numpy array
    input_data_np = np.array(numbers).reshape(1, -1)

    # Make predictions
    predictions = model.predict(input_data_np)

    # Return predictions as JSON
    return {"predictions": predictions.tolist()}
