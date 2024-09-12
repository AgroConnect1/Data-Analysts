# Crop Recommendation Model API Documentation

## Overview

This API is designed to provide crop recommendations based on soil and environmental factors such as nitrogen (N), 
phosphorus (P), potassium (K), temperature, humidity, pH, and rainfall. The API uses a machine learning model, specifically 
a RandomForestClassifier, to predict the best crop for given inputs. Additionally, the API offers endpoints for dataset management,
model training, evaluation, and crop prediction.

#### Base URL

	http://example.com/

---

### **1. Upload Data**

Uploads the dataset that will be used for crop recommendation model training and predictions.

-   **Endpoint**: `/upload_data`
-   **Method**: `POST`
-   **Description**: Uploads a CSV file that contains the crop dataset.

#### **Request:**

-   **Content-Type**: `multipart/form-data`
-   **Body Parameters**:
    -   `file` (CSV): The CSV file with the following columns:
        -   `N`: Nitrogen content (int)
        -   `P`: Phosphorus content (int)
        -   `K`: Potassium content (int)
        -   `temperature`: Temperature in Celsius (float)
        -   `humidity`: Humidity percentage (float)
        -   `ph`: pH level of the soil (float)
        -   `rainfall`: Rainfall in mm (float)
        -   `label`: Crop type (string)

#### **Response**:

```json
{
  "status": "success",
  "message": "Data uploaded successfully"
}
```  

---

### **2. Train Model**

Trains or retrains the crop recommendation model with the provided dataset.

-   **Endpoint**: `/train_model`
-   **Method**: `POST`
-   **Description**: Trains the model using the uploaded data. This must be called after data upload.

#### **Request**:

No parameters required. Training will begin automatically once this endpoint is called.

#### **Response**:

```json
{
  "status": "success",
  "message": "Model trained successfully",
  "accuracy": 0.99
}
```
---
### **3. Predict Crop**

Predicts the best-suited crop based on the given environmental and soil conditions.

-   **Endpoint**: `/predict_crop`
-   **Method**: `POST`
-   **Description**: Returns a crop recommendation based on the input values provided for soil and environmental conditions.

#### **Request:**
```json
{
  "N": 90,
  "P": 40,
  "K": 50,
  "temperature": 22.5,
  "humidity": 80.0,
  "ph": 6.5,
  "rainfall": 150.0
}
```
#### **Response:**

```json
{
  "status": "success",
  "recommended_crop": "rice"
}
```
---
### **4. Get Available Crops**

Fetches the list of crop types that the model is trained to predict.

-   **Endpoint**: `/get_crops`
-   **Method**: `GET`
-   **Description**: Returns the list of crops that the model can predict.


#### **Response**:
```json
{
  "status": "success",
  "crops": [
    "rice",
    "maize",
    "jute",
    "cotton",
    "coconut",
    "papaya",
    "..."
  ]
}
```
---

### **5. Reset Data**

Resets the current data and model to start fresh.

-   **Endpoint**: `/reset_data`
-   **Method**: `POST`
-   **Description**: Clears the uploaded dataset and model, allowing for a fresh upload and retraining.

#### **Response**:

```json
{
  "status": "success",
  "message": "Data and model reset successfully"
}
```
---
### **Example Workflow**

1.  **Upload Data**: `POST /upload_data`
2.  **Train Model**: `POST /train_model`
3.  **Make Prediction**: `POST /predict_crop`
---


## Schema Crop

| Attribute   	| Type   	| Description                					        |
|-------------	|--------	|--------------------------------------	    |
| N           	    | int    		| ratio of Nitrogen content in soil    	|
| P                   	| int    		| ratio of Phosphorous content in soil |
| K                	| int    		| ratio of Potassium content in soil   	|
| temperature | float  	| temperature in Celsius        	|
| humidity    	| float  	| relative humidity in %               			|
| ph          		| float  	| Soil pH value           			      	|
| rainfall   	 	| float  	| Rainfall in mm                   			    	|
| label    		   	| object 	| Crop label                              						       	|


