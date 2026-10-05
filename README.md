# 🛒 Retail Sales Analytics & Forecasting

## 📝 Overview
An end-to-end Data Analytics and Machine Learning project designed to analyze retail sales, perform customer/product analysis, and forecast future sales. This project takes raw retail data and transforms it into actionable business insights through a comprehensive pipeline, culminating in an interactive Streamlit web dashboard and Power BI reports.

## 🎯 Objectives
- **Data Analytics:** Clean and explore historical sales data to understand trends, profitability, and customer behavior.
- **Machine Learning:** Engineer features and build predictive models to forecast future sales with high accuracy.
- **Business Intelligence:** Provide an interactive Executive Dashboard for stakeholders to easily monitor KPIs and make data-driven decisions.

## 🛠️ Technologies Used
- **Programming:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn, XGBoost, Joblib
- **Data Visualization:** Matplotlib, Plotly, Streamlit
- **BI Tools:** Power BI (for additional reporting)

## 📂 Project Structure
The project follows a structured Jupyter Notebook pipeline:
- `01_Data_Loading_and_Understanding.ipynb`: Initial data ingestion and basic understanding.
- `02_Data_Cleaning_and_Preprocessing.ipynb`: Handling missing values, duplicates, and data typing.
- `03_Exploratory_Data_Analysis.ipynb`: Deep dive into sales trends, category performance, and geographical distribution.
- `04_Feature_Engineering.ipynb`: Creating new temporal and categorical features to improve model accuracy.
- `05_Machine_Learning_Model_Building.ipynb`: Training and tuning regression models to predict sales.
- `06_Model_Evaluation_and_Sales_Forecasting.ipynb`: Evaluating model performance (R², RMSE, MAE) and generating future forecasts.
- `Interface.py`: The interactive Streamlit web application.
- `req.txt`: All necessary Python dependencies.

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/RaviYadav1818/Retail-sales-analysis-and-Forecasting.git
   cd Retail-sales-analysis-and-Forecasting
   ```

2. **Install the dependencies**
   ```bash
   pip install -r req.txt
   ```

3. **Run the Streamlit Dashboard**
   ```bash
   streamlit run Interface.py
   ```

## 📊 Dashboard Features
- **Executive Dashboard:** High-level KPIs including Total Sales, Total Profit, Orders, and Customers.
- **Product Analysis:** Top/bottom performing products and category-level sales breakdowns.
- **Customer Analysis:** Insights into customer segments, growth, and repeat buyers.
- **Regional Analysis:** Geographical mapping of sales and profits across different states and regions.
- **Sales Forecasting:** Actual vs. Predicted sales visualizations and future monthly forecasts.
