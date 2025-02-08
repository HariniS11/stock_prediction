import streamlit as st
import pickle
import numpy as np
import pandas as pd
import mlflow
import matplotlib.pyplot as plt

# Set MLflow tracking URI
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Load MLflow Model
model_name = "linear_regression"
version = 1  
model_uri = f"models:/{model_name}/{version}"
model = mlflow.pyfunc.load_model(model_uri)

# Load Scalers
with open('scaler_file.pkl', 'rb') as f:
    scaler_file = pickle.load(f)

with open('scaler_close.pkl', 'rb') as f:
    scaler_close = pickle.load(f)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Prediction", "Visualization"])

# Initialize session state for storing inputs
if "user_inputs" not in st.session_state:
    st.session_state.user_inputs = []
if "predicted_values" not in st.session_state:
    st.session_state.predicted_values = []

# ---- PREDICTION PAGE ----
if page == "Prediction":
    def stock_prediction(input_data):
        """Predicts the close price based on the given input features."""
        prediction_scaled = model.predict(input_data)
        predicted_value = scaler_close.inverse_transform(np.array(prediction_scaled).reshape(-1, 1))
        return predicted_value[0][0]

    st.title('📈 STOCK PRICE PREDICTION')

    # User Input for Features
    company = st.selectbox("Select Company", ["Amazon", "Apple", "Facebook", "Google", "Netflix"])
    
    open_price = st.number_input("Enter Open Price", value=0.0)
    high_price = st.number_input("Enter High Price", value=0.0)
    low_price = st.number_input("Enter Low Price", value=0.0)
    volume = st.number_input("Enter Volume", value=0.0)

    # One-Hot Encoding for Company
    company_list = ["Amazon", "Apple", "Facebook", "Google", "Netflix"]
    company_encoded = [1 if company == c else 0 for c in company_list]
    company_encoded_2d = np.array(company_encoded).reshape(1, -1) 
    
    # Prepare Data for Scaling
    raw_features = np.array([[open_price, high_price, low_price, volume]])
    scaled_features = scaler_file.transform(raw_features)
    final_features = np.concatenate((scaled_features, company_encoded_2d), axis=1)

    # Convert to DataFrame
    input_data = pd.DataFrame(final_features, columns=['Open', 'High', 'Low', 'Volume',
                                                       'Company_Amazon', 'Company_Apple',
                                                       'Company_Facebook', 'Company_Google', 'Company_Netflix'])

    # Predict
    if st.button('Predict'):
        result = stock_prediction(input_data)
        st.success(f'📉 The Predicted Close Price is **{result:.2f}**')

        # Store user input & prediction in session state
        st.session_state.user_inputs.append(open_price)
        st.session_state.predicted_values.append(result)

# ---- VISUALIZATION PAGE ----
elif page == "Visualization":
    st.title("📊 Prediction Visualization")

    if len(st.session_state.user_inputs) == 0:
        st.warning("⚠️ No predictions available! Please go to the Prediction page first.")
    else:
        # Plot User Inputs (X-axis) vs. Predicted Close Prices (Y-axis)
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(st.session_state.user_inputs, st.session_state.predicted_values, color='b', marker='o', label="Predicted Close Price")
        ax.plot(st.session_state.user_inputs, st.session_state.predicted_values, linestyle='--', color='r')

        ax.set_xlabel("User Input (Open Price)")
        ax.set_ylabel("Predicted Close Price")
        ax.set_title("Predicted Close Price vs Open Price")
        ax.legend()
        
        st.pyplot(fig)
