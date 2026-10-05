import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Retail Sales Analytics & Forecasting",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>

.main {
    background-color: #F8F9FA;
}

.title{
    font-size:40px;
    font-weight:bold;
    color:#1F4E79;
}

.subtitle{
    font-size:20px;
    color:gray;
}

.card{
    background-color:white;
    padding:20px;
    border-radius:15px;
    box-shadow:2px 2px 10px rgba(0,0,0,0.15);
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "Select Dashboard",
    (
        "🏠 Home",
        "📈 Executive Dashboard",
        "📦 Product Analysis",
        "👥 Customer Analysis",
        "🌍 Regional Analysis",
        "🤖 Sales Forecasting",
        "📋 Model Performance",
        "ℹ About"
    )
)

st.sidebar.markdown("---")

st.sidebar.header("Filters")

st.sidebar.selectbox(
    "Year",
    ["All","2019","2020","2021","2022"]
)

st.sidebar.selectbox(
    "Region",
    ["All","East","West","Central","South"]
)

st.sidebar.selectbox(
    "Category",
    ["All","Furniture","Office Supplies","Technology"]
)

st.sidebar.selectbox(
    "Segment",
    ["All","Consumer","Corporate","Home Office"]
)

st.sidebar.markdown("---")

st.sidebar.success("Retail Sales Analytics Project")

# ----------------------------
# HOME
# ----------------------------

if page=="🏠 Home":

    st.markdown("<p class='title'>📊 Retail Sales Analytics & Forecasting</p>", unsafe_allow_html=True)

    st.markdown("<p class='subtitle'>End-to-End Retail Sales Analytics using Python, Machine Learning and Power BI</p>", unsafe_allow_html=True)

    st.divider()

    col1,col2,col3=st.columns(3)

    with col1:

        st.info("""
### 🎯 Objective

Analyze retail sales

Forecast future sales

Create business dashboard
""")

    with col2:

        st.success("""
### 🛠 Technologies

Python

Pandas

Scikit-Learn

Power BI

Streamlit
""")

    with col3:

        st.warning("""
### 📂 Dataset

Retail Sales Dataset

10,000+ Records

Sales Forecasting
""")

    st.divider()

    st.subheader("Project Workflow")

    st.code("""
Retail Dataset
      │
      ▼
Data Cleaning
      │
      ▼
EDA
      │
      ▼
Feature Engineering
      │
      ▼
Machine Learning
      │
      ▼
Sales Forecasting
      │
      ▼
Power BI Dashboard
      │
      ▼
Streamlit Dashboard
""")

# ----------------------------
# EXECUTIVE DASHBOARD
# ----------------------------

elif page=="📈 Executive Dashboard":

    st.title("📈 Executive Dashboard")

    c1,c2,c3,c4,c5=st.columns(5)

    c1.metric("💰 Total Sales","₹2.30M","+8%")
    c2.metric("📈 Total Profit","₹286K","+12%")
    c3.metric("📦 Orders","9,994","+4%")
    c4.metric("👥 Customers","793","+3%")
    c5.metric("🛒 Quantity","37,873","+5%")

    st.divider()

    left,right=st.columns(2)

    with left:

        st.info("📊 Monthly Sales Trend")

        st.empty()

    with right:

        st.info("📍 Sales by Region")

        st.empty()

    left,right=st.columns(2)

    with left:

        st.info("📦 Category Sales")

        st.empty()

    with right:

        st.info("📈 Profit Analysis")

        st.empty()

# ----------------------------
# PRODUCT
# ----------------------------

elif page=="📦 Product Analysis":

    st.title("📦 Product Analysis")

    col1,col2=st.columns(2)

    with col1:

        st.info("🏆 Top 10 Products")

        st.empty()

    with col2:

        st.info("📉 Bottom 10 Products")

        st.empty()

    st.divider()

    col1,col2=st.columns(2)

    with col1:

        st.info("📊 Category Analysis")

        st.empty()

    with col2:

        st.info("📈 Sub Category Analysis")

        st.empty()

# ----------------------------
# CUSTOMER
# ----------------------------

elif page=="👥 Customer Analysis":

    st.title("👥 Customer Analysis")

    c1,c2,c3=st.columns(3)

    c1.metric("Customers","793")
    c2.metric("Repeat Customers","620")
    c3.metric("Customer Growth","12%")

    st.divider()

    st.info("🏆 Top Customers")

    st.empty()

    st.info("📊 Customer Segments")

    st.empty()

# ----------------------------
# REGION
# ----------------------------

elif page=="🌍 Regional Analysis":

    st.title("🌍 Regional Analysis")

    st.info("🗺 State Wise Sales")

    st.empty()

    st.info("📍 Region Wise Sales")

    st.empty()

    st.info("🌎 Geographic Map")

    st.empty()

# ----------------------------
# FORECAST
# ----------------------------

elif page=="🤖 Sales Forecasting":

    st.title("🤖 Sales Forecasting")

    c1,c2,c3=st.columns(3)

    c1.metric("Actual Sales","₹2.30M")
    c2.metric("Predicted Sales","₹2.28M")
    c3.metric("Accuracy","95%")

    st.divider()

    st.info("📈 Actual vs Predicted Sales")

    st.empty()

    st.info("📊 Monthly Forecast")

    st.empty()

# ----------------------------
# MODEL
# ----------------------------

elif page=="📋 Model Performance":

    st.title("📋 Model Performance")

    st.metric("R² Score","0.95")
    st.metric("RMSE","38.47")
    st.metric("MAE","30.50")

    st.divider()

    st.info("🏆 Model Comparison")

    st.empty()

    st.info("📊 Feature Importance")

    st.empty()

# ----------------------------
# ABOUT
# ----------------------------

else:

    st.title("ℹ About")

    st.write("""
### End-to-End Retail Sales Analytics & Forecasting

This project demonstrates:

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning
- Sales Forecasting
- Power BI Dashboard
- Streamlit Dashboard

Developed using:

- Python
- Pandas
- Scikit-Learn
- Streamlit
- Power BI
""")

st.markdown("---")
st.markdown("<p class='footer'>© 2026 Retail Sales Analytics Dashboard</p>", unsafe_allow_html=True)