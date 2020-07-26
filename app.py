import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from plots import *

plots_list = {'Histogram': plot_histogram, 'Scatter Plot': plot_scatterplot}
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
    
    target_col = st.sidebar.selectbox(
        'Select Target Column',
        (None,(*list(df.columns)))
        )
    if target_col is not None:
        if st.checkbox('Target Histogram', value=1):
            plot_histogram(df, target_col, target_col)
    
    plot = st.sidebar.selectbox(
        'Select Plot',
        (None, (*plots_list.keys()))
    )
    if plot:
        xcol = st.sidebar.selectbox(
            'Select x axis column',
            (None,(*list(df.columns)))
        )
        ycol = st.sidebar.selectbox(
            'Select y axis column',
            (None,(*list(df.columns)))
        )
        color = st.sidebar.selectbox(
            'Select color axis column',
            (None,(*list(df.columns)))
        )
        if xcol is not None:
            plots_list[plot](df, xcol, ycol, color)


else:
    st.info("Select or upload a dataset")
