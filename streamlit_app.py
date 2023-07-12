# -*- coding: utf-8 -*-
"""streamlit_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13xbRVMHzExlJ45FqeZvGc1XhrK-2Rt-5
"""

import streamlit as st

import numpy as np
import pandas as pd




def get_predict(dataset):
  return 39.391830*dataset.loc[:, 'Mor28p:(MORDRED)'] + 26.446247*dataset.loc[:, 'Mor13se:(MORDRED)'] + 53.579802*dataset.loc[:, 'Mor26m:(MORDRED)'] - 0.330472*dataset.loc[:, 'PEOE_VSA7:(MORDRED)'] - 1.235251*dataset.loc[:, 'SsOH:(MORDRED)'] + 3.458921*dataset.loc[:, 'PEOE_VSA5:(MORDRED)'] - 336.598009*dataset.loc[:, 'GATS1d:(MORDRED)'] + 64.284856*dataset.loc[:, 'AATSC4dv:(MORDRED)'] + 350.2463171947596


st.title("QSAR prediction of inhibition of peroxidation oxidation")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)

st.write(get_predict(df))
