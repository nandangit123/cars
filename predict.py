import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,mean_squared_log_error
@st.cache()
# Define the 'prediction()' function.
def prediction(car_df,carwidth, enginesize, horsepower, drivewheel_fwd, car_company_buick):
  x = car_df.iloc[:,:-1]
  y = car_df['price']
  X_train,X_test,y_train,y_test = train_test_split(x,y,test_size = 0.33,random_state = 42)
  lr = LinearRegression()
  lr.fit(X_train,y_train)
  score = lr.score(X_train,y_train)
  price = lr.predict([[carwidth, enginesize, horsepower, drivewheel_fwd, car_company_buick]])
  price = price[0]
  y_test_pred = lr.predict(X_test)
  test_r2score = r2_score(y_test,y_test_pred)
  test_mae = mean_absolute_error(y_test,y_test_pred)
  test_msle = mean_squared_log_error(y_test,y_test_pred)
  test_rmse = np.sqrt(mean_squared_error(y_test,y_test_pred))
  return price,score,test_r2score,test_mae,test_msle,test_rmse

def app(car_df):
  st.markdown("<p style = 'color : blue; font-size : 25px'> This app uses <b> linear regression </b> to predict the price of a car based on your inputs.",unsafe_allow_html = True)
  st.subheader("Select values : ")
  car_wid = st.slider("carwidth",float(car_df['carwidth'].min()),float(car_df['carwidth'].max()))
  car_eng = st.slider("engensize",float(car_df['enginesize'].min()),float(car_df['enginesize'].max()))
  car_horse = st.slider("horsepower",float(car_df['horsepower'].min()),float(car_df['horsepower'].max()))
  car_drw_fwd = st.radio("Is it a forward drive wheel car?",("Yes","No"))
  if car_drw_fwd == 'No':
    car_drw_fwd = 0
  else:
    car_drw_fwd = 1
  com_bui = st.radio("Is the car manufacture by buick?",("Yes","No"))
  if com_bui == "No":
    com_bui = 0
  else:
    com_bui = 1
  if st.button("Predict"):
    st.subheader("Prediction results")
    price,score,car_r2score,car_mae,car_msle,car_rmse = prediction(car_df,car_wid,car_eng,car_horse,car_drw_fwd,com_bui)
    st.success("Predicted price of the car is : ${:,}".format(int(price)))
    st.info("Accuracy score of this model is : {:2.2%}".format(score))
    st.info(f"R sqaured score of this model is : {car_r2score:.3f}")
    st.info(f"Mean absolute error of this model is : {car_mae:.3f}")
    st.info(f"Mean squared log error of this model is : {car_msle:.3f}")
    st.info(f"Mean root squared error of this model is : {car_rmse:.3f}")