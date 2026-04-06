import os
import streamlit as st
import numpy as np
import pandas as pd
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

st.set_page_config(page_title="Wine Quality Model", layout='centered')

st.title("Predict Wine Quality")
st.write("This app predicts the Wine quality based on the following set of features, using an ElasticNet Machine learning Regression Model.")

if "training_status" not in st.session_state:
    st.session_state.training_status = False

if not st.session_state.training_status:
    with st.spinner("Training the Model..."):
        os.system("python main.py")
    st.session_state.training_status = True

fixed_acidity = st.number_input(label="Fixed Acidity")
volatile_acidity = st.number_input("Volatile Acidity")
citric_acid =st.number_input("Citric Acid")
residual_sugar =st.number_input("Residual Sugar")
chlorides =st.number_input("Chlorides")
free_sulfur_dioxide =st.number_input("Free Sulphur Dioxide")
total_sulfur_dioxide =st.number_input("Total Sulphur Dioxide")
density =st.number_input("Density")
pH =st.number_input("pH")
sulphates =st.number_input("Sulphates")
alcohol =st.number_input("Alcohol")

data = [[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]]

data = np.array(data)

st.divider()


if st.button("Predict Wine Quality"):
    with st.spinner("Predicting..."):
        obj = PredictionPipeline()
        prediction = obj.predict(data)

    st.success(f"The Predicted Qauality is: {int(np.round(prediction, 0)[-1])}")