import streamlit as st
import requests
import pandas as pd
import time

st.title("Real-Time Fraud Detection Dashboard")

placeholder=st.empty()

while True:
    response=requests.get('http://localhost:8000/predict-stream').json()
    df=pd.DataFrame(response)
    with placeholder.container():
        st.write('Recent Predictions:')
        st.dataframe(df)
    time.sleep(5)