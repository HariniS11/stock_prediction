# Stock Price Prediction Using Decision Tree and Linear Regression

## 📌 Project Overview
This project focuses on predicting the stock prices of major companies like **Apple**, **Amazon**, **Google**, and **Netflix** using **Decision Tree** and **Linear Regression** models. The models achieved an impressive accuracy of **99%**.

The goal is to provide accurate price predictions based on historical stock data. Users can input stock details, and the model will predict the stock price.

**MLflow** was used for experiment tracking and model management.

---

## 🛠️ Tech Stack
- **Python**
- **Pandas, NumPy**: For data manipulation and analysis
- **Matplotlib, Seaborn**: For data visualization
- **Scikit-Learn**: For Machine Learning models
- **MLflow**: For model tracking and management
- **Streamlit**: For developing an interactive application

---

## 🔎 Problem Statement
The objective is to predict the future stock price of a selected company based on historical stock data. Users will choose one of the supported companies, and the model will return an accurate price prediction.

---

## 📊 Data Preprocessing
- **Missing Value Handling**: Handled using mean and median imputation.
- **Feature Engineering**: Created new features like moving averages and volatility.
- **Scaling**: Applied Min-Max Scaling to normalize data.

---

## 🚀 Project Structure
```
Stock-Price-Prediction/
├── data/
├── models/
│   ├── decision_tree_model.pkl
│   ├── linear_regression_model.pkl
├── app/
│   ├── app.py
├── notebooks/
│   ├── EDA.ipynb
│   ├── Model_Training.ipynb
├── mlruns/ (Managed by MLflow)
├── requirements.txt
├── README.md
```

---

## 📥 Installation and Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/stock-price-prediction.git
    cd stock-price-prediction
    ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit application:
    ```bash
    streamlit run app/app.py
    ```

---

## 🧑‍💻 Streamlit Application Features
- **Stock Prediction Page**: Predict stock prices for Apple, Amazon, Google, or Netflix.
- **Model Comparison Page**: Compare predictions from Decision Tree and Linear Regression models.
- **MLflow Tracking Page**: Track model performance using MLflow.

---

## ⚡ Future Improvements
- Implement additional time series models like LSTMs and ARIMA.
- Incorporate external data like financial news sentiment.
- Deploy the app on cloud platforms like AWS or Azure.

---

## 💡 Conclusion
This project provides accurate stock price predictions using Decision Tree and Linear Regression models with **99% accuracy**. MLflow streamlines model management and ensures efficient tracking of performance.

---

## 🤝 Acknowledgments
- Dataset Source: [Provide Dataset Link]
- Libraries: Scikit-Learn, Streamlit, Matplotlib, MLflow, Pandas

---

## 📬 Contact
For queries or feedback, feel free to reach out through GitHub or email.


