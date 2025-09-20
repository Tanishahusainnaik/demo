import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

# ------------------- THEME  -------------------
custom_css = """
<style>
/* Background */
body {
    background-color: #E7EBEF;
    font-family: 'Segoe UI Semibold', Helvetica, Arial, sans-serif;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #1673BA;
    color: white;
}
section[data-testid="stSidebar"] .css-1lcbmhc, 
section[data-testid="stSidebar"] .css-qbe2hs {
    color: white;
}

/* Titles */
h1, h2, h3 {
    color: #1673BA;
    font-family: 'Segoe UI Semibold', Helvetica, Arial, sans-serif;
}

/* Labels */
label, .stTextInput label, .stNumberInput label, .stSelectbox label {
    font-size: 12px;
    color: #293537;
}

/* Buttons */
div.stButton > button {
    background-color: #4896FE;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 8px 16px;
    font-size: 14px;
    font-weight: bold;
    transition: 0.3s;
}
div.stButton > button:hover {
    background-color: #1673BA;
    color: #fff;
}

/* Info boxes */
.stAlert {
    background-color: #F4D25A20;
    color: #293537;
    border-left: 6px solid #D9B300;
}

/* Success & Warning */
.stAlert.success {
    background-color: #16C8C720;
    border-left: 6px solid #16C8C7;
}
.stAlert.warning {
    background-color: #D6455020;
    border-left: 6px solid #D64550;
}

/* DataFrame tables */
.dataframe th {
    background-color: #1673BA !important;
    color: white !important;
}
.dataframe td {
    background-color: #FFFFFF !important;
    color: #293537 !important;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ------------------- COLOR PALETTE -------------------
custom_palette = ["#1673BA","#74C3FF","#4896FE","#16C8C7","#60E8E8",
                  "#E7EBEF","#D9B300","#D64550","#3599B8","#DFBFBF"]

sns.set_palette(custom_palette)

# ------------------- SIDEBAR -------------------
st.sidebar.title("🏥 Hospital Management System")
page = st.sidebar.radio("Go to", ["Home", "Patient Predictions", "Capacity Planning", "Quality & Safety"])

# ------------------- HOME -------------------
if page == "Home":
    st.title("🏥 Hospital Management Dashboard")
    st.write("Welcome to the Hospital Management System built with *Streamlit*.")
    st.write("This app provides:")
    st.markdown("""
    - 📊 Predicting patient Length of Stay (LOS) & Readmission Risk  
    - 🛏 Capacity Planning (bed demand & staffing recommendations)  
    - ✅ Monitoring Quality & Safety indicators  
    """)

    st.subheader("Dataset Overview")
    st.info("📂 Data preview will be shown here once connected.")

    # Example styled table
    df = pd.DataFrame({
        "Unit": ["ICU", "Surgical", "Medical"],
        "Beds Occupied": [12, 30, 25]
    })
    st.dataframe(df)

# ------------------- PATIENT PREDICTIONS -------------------
elif page == "Patient Predictions":
    st.title("🤖 Patient Predictions")
    st.write("Enter patient details to get predictions (to be connected with backend later).")

    # Patient details form
    st.subheader("Patient Information")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 0, 120, 45)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    with col2:
        admission_type = st.selectbox("Admission Type", ["Emergency", "Elective", "Urgent"])
        diagnosis = st.text_input("Diagnosis")

    if st.button("Predict"):
        st.success("Predictions will appear here once backend is integrated.")

# ------------------- CAPACITY PLANNING -------------------
elif page == "Capacity Planning":
    st.title("📈 Capacity Planning")
    st.write("Visualizations of bed demand & staffing will appear here.")

    st.subheader("Bed Occupancy by Unit")
    df = pd.DataFrame({
        "Unit": ["ICU", "Surgical", "Medical"],
        "Beds": [12, 30, 25]
    })
    chart = alt.Chart(df).mark_bar().encode(
        x="Unit",
        y="Beds",
        color=alt.Color("Unit", scale=alt.Scale(range=custom_palette))
    )
    st.altair_chart(chart, use_container_width=True)

    st.subheader("Daily Admissions Trend")
    df2 = pd.DataFrame({
        "Day": pd.date_range("2025-01-01", periods=7),
        "Admissions": [10, 15, 18, 12, 20, 22, 19]
    })
    fig, ax = plt.subplots()
    sns.lineplot(data=df2, x="Day", y="Admissions", ax=ax, marker="o")
    st.pyplot(fig)

# ------------------- QUALITY & SAFETY -------------------
elif page == "Quality & Safety":
    st.title("✅ Quality & Safety Monitors")
    st.write("Track infection rates, adverse events, and satisfaction trends.")

    st.subheader("Infection Rate Distribution")
    data = pd.DataFrame({"Infection Rate": [2, 3, 5, 4, 6, 7, 3, 4, 5, 6]})
    fig, ax = plt.subplots()
    sns.histplot(data["Infection Rate"], bins=5, ax=ax, color="#D64550")
    st.pyplot(fig)

    st.subheader("Patient Satisfaction Trends")
    df3 = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Satisfaction": [70, 75, 80, 78, 85]
    })
    chart2 = alt.Chart(df3).mark_line(point=True).encode(
        x="Month",
        y="Satisfaction",
        color=alt.value("#16C8C7")
    )
    st.altair_chart(chart2, use_container_width=True)

    st.subheader("Readmission Rate by Gender")
    df4 = pd.DataFrame({
        "Gender": ["Male", "Female"],
        "Readmission Rate": [12, 15]
    })
    fig, ax = plt.subplots()
    sns.barplot(data=df4, x="Gender", y="Readmission Rate", palette=custom_palette)
    st.pyplot(fig)
