import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(df, xcol=None,y_col=None, color = None):
    if color is None:
        color = xcol
    fig = px.histogram(df, x=xcol, title= 'Target column Histogram', 
                                color = color, color_discrete_sequence= px.colors.sequential.Viridis)
    st.plotly_chart(fig)

def plot_scatterplot(df, xcol= None, ycol = None, color = None):
    fig = px.scatter(df, xcol, ycol, color, color_discrete_sequence= px.colors.sequential.Viridis)
    st.plotly_chart(fig)

def plot_boxplot(df, xcol=None, ycol = None, color = None):
    if color is None:
        color = xcol
    fig = px.box(df, xcol, ycol, color, color_discrete_sequence= px.colors.sequential.Viridis)
    st.plotly_chart(fig)