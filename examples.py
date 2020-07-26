import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

example_datasets = [None, 'winequality.csv', 'heart.csv']
st.title('Dataset Dashboard')
option = st.sidebar.selectbox(
    'Select from example datasets',
    example_datasets)

uploaded_file = st.sidebar.file_uploader('Upload a csv file')
if uploaded_file:
    option = uploaded_file


def load_data(option):
    df = pd.read_csv(option)
    return df
if option:
    df = load_data(option)
    if st.checkbox('First Five rows', value=1):
        st.write(df.head())
    #cols = 
    target_col = st.sidebar.selectbox(
        'Select Target Column',
        (None,(*list(df.columns)))
        )
    if target_col is not None:
        if st.checkbox('Target Histogram', value=1):
            fig = px.histogram(df, x=target_col, title= 'Target column Histogram')
            st.plotly_chart(fig)

else:
    st.info("Select or upload a dataset")