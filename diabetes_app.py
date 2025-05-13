import streamlit as st
import plotly.express as px
import pandas as pd

data = pd.read_csv("diabetes.csv")

# print(data)

st.set_page_config(page_title="diabetes_dashboard",layout="wide")
st.title("DiabetesDashboard")
st.subheader("Diabetes_stat")
tab1,tab2,tab3=st.tabs(["Glucose","BMI","BloodPressure"])
with tab1:
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Glucose analysis")
        g = data["Glucose"]
        m = g.mean()
        m = round(m,2)
        st.metric("avg_Glucose",m)
    with col2:
        fig1 =px.histogram(data,x="Glucose",nbins=40,color_discrete_sequence=["#f5e680"])
        fig1.update_layout(title="Glucose histogram",xaxis_title= "Glucose",yaxis_title= "counts" )
        st.plotly_chart(fig1)


with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("BMI analysis")
        g = data["BMI"]
        m =g.mean()
        m =round(m,2)
        st.metric("avg_BMI",m)
    with col2:
        fig2 =px.histogram(data,x="BMI",nbins=40,color_discrete_sequence=["#7aff33"])
        fig2.update_layout(title="BMI histogram",xaxis_title="BMI",yaxis_title="counts")
        st.plotly_chart(fig2)

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("BloodPressure analysis")
        g = data["BloodPressure"]
        m = g.mean()
        m = round(m, 2)
        st.metric("avg_BloodPressure",m)

    with col2:
        fig3=px.histogram(data,x="BloodPressure",nbins=30,color_discrete_sequence=["#ff3633"])
        fig3.update_layout(title="BloodPressure",xaxis_title="BloodPressure",yaxis_title="counts")
        st.plotly_chart(fig3)
