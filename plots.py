import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.header("Visualise Data")
  st.set_option('deprecation.showPyplotGlobalUse',False)
  st.subheader("Scatterplot")
  feature_list = st.multiselect("Select the X-axis vales :",('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
  for feature in feature_list:
    st.subheader(f"Scatter plot between {feature} and price")
    plt.figure(figsize=(12,6))
    sns.scatterplot(x=feature,y='price',data = car_df)
    st.pyplot()
  st.subheader("Visualisation Selector")
  plot_types = st.multiselect("Select charts or plots :",('histogram','boxplot','Correlation heatmap'))
  if 'histogram' in plot_types:
    st.subheader("Histogram")
    columns = st.selectbox("Select the column to create its histogram",('carwidth','enginesize','horsepower'))
    plt.figure(figsize = (12,6))
    plt.title(f"Histogram for {columns}")
    plt.hist(car_df[columns],bins = 'sturges',edgecolor = 'black')
    st.pyplot()
  if 'boxplot' in plot_types:
    st.subheader("Box Plot")
    columns = st.selectbox("Select the column to create its boxplot",('carwidth','enginesize','horsepower'))
    plt.figure(figsize = (12,6))
    plt.title(f"Box Plot for {columns}")
    sns.boxplot(car_df[columns])
    st.pyplot()
  if 'Correlation heatmap' in plot_types:
    st.subheader("Correlation heatmap")
    plt.figure(figsize = (12,6))
    plt.title(f"Correlation heatmap")
    ax=sns.heatmap(car_df.corr(),annot = True)
    bottom,top = ax.get_ylim()
    ax.set_ylim(bottom+0.5,top-0.5)
    st.pyplot()  