import streamlit as st
import pickle
import pandas as pd
import numpy as np
import json


transformer = pickle.load(open("models/transformer.pkl","rb"))
pipeline = pickle.load(open("models/pipe.pkl","rb"))

with open ('column_names.json','r') as json_file:
    column_names = json.load(json_file)


st.title("Thyroid Cancer Recurrence Prediction")

st.subheader('Select patient details ', divider='grey')

Age = st.number_input("Patient's Age", value=None, placeholder="Type patient's age")


Gender = st.selectbox(
    "What is the patient's gender?",
    ('M', 'F'),index=None)

Hx_smoking = st.selectbox(
    "History of Smoking?",
    ('Yes', 'No'),index=None)

Hx_radio = st.selectbox(
    "History of Radio Therapy?",
    ('Yes', 'No'),index=None)

smoking = st.selectbox(
    "Does the patient smoke currently?",
    ('Yes', 'No'),index=None)

thyroid = st.selectbox(
    "What is the patient's thyroid functioning?",
    ('Euthyroid', 'Clinical Hyperthyroidism','Subclinical Hypothyroidism', 'Clinical Hypothyroidism','Subclinical Hyperthyroidism'),index=None)

physical = st.selectbox(
    "Findings of Physical Examination",
    ('Normal', 'Single nodular goiter-right','Single nodular goiter-left', 'Diffuse goiter','Multinodular goiter'),index=None)

Adenopathy = st.selectbox(
    "Patient Adenopathy",
    ('No', 'Right','Left', 'Posterior','Bilateral','Extensive'),index=None)

pathology = st.selectbox(
    "Patient Pathology",
    ('Papillary', 'Micropapillary','Follicular', 'Hurthel cell'),index=None)

focality = st.selectbox(
    "Patient focality",
    ('Uni-Focal', 'Multi-Focal'),index=None)

risk = st.selectbox(
    "Patient Risk",
    ('Low', 'Intermediate','High'),index=None)

T = st.selectbox(
    "Patient T-stage",
    ('T1a', 'T1b', 'T2','T3a', 'T3b', 'T4a', 'T4b'),index=None)

N = st.selectbox(
    "Patient N-stage",
    ('N0', 'N1a', 'N1b'),index=None)

M = st.selectbox(
    "Patient M-stage",
    ('M0', 'M1'),index=None)

stage = st.selectbox(
    "Patient Cancer stage",
    ('I', 'II','III','IVA','IVB'),index=None)

response = st.selectbox(
    "Patient Response",
    ('Excellent', 'Structural Incomplete','Indeterminate','Biochemical Incomplete'),index=None)

data = [Age , Gender , smoking, Hx_smoking, Hx_radio,
        thyroid, physical, Adenopathy, pathology, focality,
        risk, T, N, M, stage, response]

if None not in data:
    data = np.array(data,dtype=object).reshape(1,-1)
    data = pd.DataFrame(data,columns=column_names)
    data = transformer.transform(data)
    pred = pipeline.predict(data)

    if pred == 0:
        st.success("The cancer is predicted to **not recur**.")

    elif pred == 1:
        st.error("The cancer is predicted to **recur**.")



