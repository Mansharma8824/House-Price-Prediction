from flask import Flask, render_template,request
import pickle
import json
import numpy as np
import pandas as pd

app = Flask(__name__)

# load the ML model
model = pickle.load(open("models/house_price_pred_model.pkl","rb"))

# Load scaler
scaler = pickle.load(open("models/scaler.pkl", "rb"))

# Load colums 
with open("models/columns.json","r") as f:
    data_columns = json.load(f)["data_columns"]

# Get locations columns from data_columns    
locations = data_columns[4:]
locations = [loc.replace("location_", "") for loc in locations]

@app.route("/")
def home():
    return render_template('index.html', locations = locations)

@app.route("/predict", methods = ['POST'])
def price_predict():
    # geting the values from the form
    sqft = float(request.form['total_sqft'])
    bath = float(request.form['bath'])
    balcony = float(request.form['balcony'])
    bhk = int(request.form['bhk'])
    location = request.form["location"]
    
    # created vectors of columns
    column_vector = np.zeros(len(data_columns))
    column_vector[data_columns.index("total_sqft")] = sqft
    column_vector[data_columns.index("bath")] = bath
    column_vector[data_columns.index("balcony")] = balcony
    column_vector[data_columns.index("bhk")] = bhk
    
    # Create location column name
    location_column = "location_" + location
    
    # check if filled location if available in columns
    if location_column in data_columns:
        loc_index = data_columns.index(location_column)
        column_vector[loc_index] = 1
    else:
        other_index = data_columns.index("location_other")
        column_vector[other_index] = 1
        
    # Convert to DataFrame
    input_df = pd.DataFrame(
        [column_vector],
        columns=data_columns
    )
    
    column_vector_scaled = scaler.transform(input_df)
    # make Prediction
    prediction = model.predict(column_vector_scaled)[0]

    # get the result
    return render_template(
        "index.html",
        prediction_text=f"Estimated Price: {round(prediction, 2)} Lakhs",
        locations=locations
    )
    


if __name__ == "__main__":
    app.run(debug=True)