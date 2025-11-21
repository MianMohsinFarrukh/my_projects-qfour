import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("🩺 AI-Powered Personal Health Monitor")

st.header("Health Score")
st.progress(75)  # Placeholder

st.header("Vitals")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Blood Pressure")
    # Placeholder chart
    chart_data = pd.DataFrame(
        {
            "Systolic": [120, 122, 121, 123, 120],
            "Diastolic": [80, 81, 79, 82, 80],
        }
    )
    st.line_chart(chart_data)

with col2:
    st.subheader("Blood Sugar")
    # Placeholder chart
    chart_data = pd.DataFrame(
        {
            "Blood Sugar": [90, 95, 88, 92, 91],
        }
    )
    st.line_chart(chart_data)


st.header("Symptoms")
# Placeholder
st.bar_chart({"headache": 3, "fatigue": 5, "nausea": 2})


st.header("Medicine Adherence")
st.progress(90)  # Placeholder

st.header("Weekly AI Summary")
st.text("Your health has been stable this week. Keep up the good work!")
