import numpy as np
import pandas as pd
import streamlit as st
def app(car_df):
    # Displaying orginal dataset
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    with st.expander("View Dataset"):
        st.table(car_df)

    # Display descriptive statistics.
    st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(car_df.describe())

    # ADD NEW CODE FROM HERE
    beta_col1,beta_col2,beta_col3 = st.columns(3)
    with beta_col1:
      if st.checkbox("Show all column names"):
        st.table(list(car_df.columns))
    with beta_col2:
      if st.checkbox("View column Data Type"):
        st.table(car_df.dtypes)
    with beta_col3:
      if st.checkbox("View column data"):
        column_data = st.selectbox('Select column',tuple(car_df.columns))
        st.write(car_df[column_data])