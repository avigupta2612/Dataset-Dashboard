import streamlit as st
import pandas as pd
#simport numpy as np
from plots import *
import os

examples_path = os.listdir('datasets/')
plots_list = {
    'Histogram': plot_histogram, 
    'Bar Chart': plot_barplot,
    'Scatter Plot': plot_scatterplot,
    'Box Plot': plot_boxplot      
}
example_datasets = [None, (*examples_path)]
st.title('Dataset Dashboard')
option = st.sidebar.selectbox(
    'Select from example datasets',
    example_datasets)
if option is not None:
    option = os.path.join('datasets',option)
uploaded_file = st.sidebar.file_uploader('Upload a csv file')
if uploaded_file:
    option = uploaded_file

@st.cache
def load_data(option):
    df = pd.read_csv(option)
    return df

if option:
    df = load_data(option)
    
    if st.checkbox('Explore Dataset', value=1):
        st.dataframe(df, 1000, 150)

    if st.sidebar.checkbox('Describe Dataset'):
        st.write(df.describe())

    target_col = st.sidebar.selectbox(
        'Select Target Column',
        (None,(*list(df.columns)))
    )

    if target_col is not None:
        if st.sidebar.checkbox('Target Histogram', value=1):
            plot_histogram(df, target_col, target_col)

    if st.sidebar.checkbox('Check for Missing Values'):
        null = df.isnull().values.any()
        if null:
            missing_values = df.isna().sum()
            missing_values = missing_values[missing_values>0]
            missing_values.sort_values(inplace=True)
            missing_values = missing_values.to_frame()
            missing_values.columns = ['Count']
            missing_values.index.names = ['Column']
            missing_values['Percentage'] = missing_values.Count.values/df.shape[0]
            missing_values['Column'] = missing_values.index
            
            plot_barplot(missing_values, xcol='Column', ycol= 'Count', color='Column', 
                        title = 'Missing Values', hover_data = [missing_values['Percentage']])
            
        else:
            st.info('No missing values')
    
    if st.sidebar.checkbox('Plot Correlation Matrix'):
        corrmap = df.corr()
        plot_heatmap(corrmap)
    
    if st.sidebar.checkbox('Create Target Distplot'):
        if target_col:
            plot_distplot(list(df[target_col].values))
        else:
            st.error("Select Target value first")
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
