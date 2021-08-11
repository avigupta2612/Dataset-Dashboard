# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:52:15 2021

@author: Sahil
"""


import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, xcol=None,y_col=None, color = None):
    if color is None:
        color = xcol
    fig = px.histogram(df, x=xcol, title= 'Histogram', 
                                color = df[color].values, color_discrete_sequence= px.colors.sequential.Viridis)
    st.plotly_chart(fig)

def plot_scatterplot(df, xcol= None, ycol = None, color = None):
    fig = px.scatter(df, xcol, ycol, color, 
                                title= 'Scatter Plot',  
                                color_discrete_sequence= px.colors.sequential.Agsunset)
    st.plotly_chart(fig)

def plot_boxplot(df, xcol=None, ycol = None, color = None):
    if color is None:
        color = xcol
    fig = px.box(df, xcol, ycol, color, 
                                title = 'Box Plot', color_discrete_sequence= px.colors.sequential.Viridis)
    st.plotly_chart(fig)

def plot_barplot(df, xcol=None, ycol= None, color= None, title = 'Bar Chart', hover_data=None):
    fig = px.bar(df, xcol, ycol, color ,
                                title= title, hover_data = hover_data,
                                color_discrete_sequence= px.colors.sequential.Plasma)
    st.plotly_chart(fig)

def plot_heatmap(df, xcol= None, ycol= None):
    plt.figure(figsize=(12,12))
    sns.heatmap(df, xcol, ycol, annot= True, cmap= 'Spectral')
    plt.title('Correlation Matrix')
    st.pyplot()

def plot_distplot(xcol):
    plt.figure(figsize=(8,5))
    sns.distplot(xcol)
    plt.title('Target Distplot')
    st.pyplot()

def pie_chart(df,xcol=None,ycol=None,color=None):
    ratio_y=df[ycol].nunique()/df[ycol].count()
    ratio_x=df[xcol].nunique()/df[xcol].count()
    if ratio_y>0.05 or ratio_x>0.05:
        st.write("Please select a column with categorical values")
    else:  
        fig=px.pie(df,values=xcol,names=ycol)
        st.plotly_chart(fig)
        