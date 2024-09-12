# Crop Recommendation Model API Documentation

## Overview

This API is designed to provide crop recommendations based on soil and environmental factors such as nitrogen (N), 
phosphorus (P), potassium (K), temperature, humidity, pH, and rainfall. The API uses a machine learning model, specifically 
a RandomForestClassifier, to predict the best crop for given inputs. Additionally, the API offers endpoints for dataset management,
model training, evaluation, and crop prediction.

#### Base URL

	https://mean-dorrie-agroconnect1-3d4965f6.koyeb.app/

---
### **Predict Crop**

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

### **Example Workflow**

**Make Prediction**: `POST /predict_crop`

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


