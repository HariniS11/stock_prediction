# **Clickstream - Customer Conversion Prediction**  

## **Project Description**  
This project focuses on analyzing customer browsing behavior using clickstream data to predict purchasing tendencies and optimize business strategies. The project tackles three core machine learning problems:  

1. **Classification:** Predict whether a customer will complete a purchase (`1`) or not (`2`).  
2. **Regression:** Estimate potential revenue per customer to enhance business revenue forecasting.  
3. **Clustering:** Segment customers based on behavior for personalized marketing and recommendations.  

By leveraging machine learning techniques, businesses can enhance user experience, improve marketing strategies, and increase conversion rates.  

---

## **Tech Stack**  
- **Python**  
- **Pandas, NumPy** (Data Preprocessing)  
- **Scikit-Learn** (Machine Learning Models)  
- **Matplotlib, Seaborn** (Data Visualization)  
- **Streamlit** (Interactive User Interface)  

---

## **Approach & Methodology**  

1. **Data Collection & Preprocessing:**  
   - Processed raw clickstream data to extract key features like session duration, number of page views, product interactions, etc.  
   - Handled missing values and outliers to improve data quality.  

2. **Feature Engineering:**  
   - Created new features from clickstream logs to improve model accuracy.  
   - Encoded categorical features and scaled numerical values.  

3. **Modeling & Evaluation:**  
   - **Classification Models:** Decision Trees, Random Forest  
     - **Decision Trees (after pruning):** **97% accuracy**  
     - **Random Forest:** **91% accuracy**  
   - **Regression Model:** Trained to estimate customer revenue.  
   - **Clustering Model:** Used k-means to segment customers into behavioral groups.  

4. **Streamlit Application:**  
   - Interactive UI for users to input customer browsing data and get predictions.  
   - Displays customer segmentation insights and revenue estimations.  

---

## **Installation Instructions**  

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/your-repo/clickstream-analysis.git  
   cd clickstream-analysis  
