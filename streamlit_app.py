# -*- coding: utf-8 -*-
"""to_streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13xbRVMHzExlJ45FqeZvGc1XhrK-2Rt-5
"""

import streamlit as st

import rdkit
from rdkit.Chem import AllChem as Chem
from rdkit.Chem import Draw
from rdkit import DataStructs
import numpy as np
import pandas as pd
import sklearn
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle
import matplotlib.pyplot as plt


from rdkit import DataStructs
from rdkit.Chem import AllChem as Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors
from rdkit.Chem import Fragments
from rdkit.Chem import rdMolDescriptors

#Выбрать похожие на берберин молекулы
def is_inEdges(dataset):
  mols = []
  smiles = []
  for i in dataset.loc[:, 'SMILES']:
    if i == str(i) and Chem.MolFromSmiles(i) != None:
      mols.append(Chem.MolFromSmiles(i))
      smiles.append(i)

  mols2 = []
  numbers = []
  index = []

  fpgen = Chem.GetRDKitFPGenerator()
  fps = [fpgen.GetFingerprint(x) for x in mols]
  for i in range(len(fps)):
    tan = (DataStructs.TanimotoSimilarity(fpgen.GetFingerprint(Chem.MolFromSmiles('COC1=C(C2=C[N+]3=C(C=C2C=C1)C4=CC5=C(C=C4CC3)OCO5)OC')), fps[i]))
    if tan > 0.45:
      #print(i, tan)
      #numbers.append(i)
      mols2.append(mols[i])
      index.append(smiles[i])

  #display(Draw.MolsToGridImage(mols2))
  #s_dataset = df.iloc[numbers, :]
  s_dataset = dataset.loc[dataset['SMILES'].isin(index)]
  return s_dataset

def get_predict(dataset):
  return 39.391830*dataset.loc[:, 'Mor28p:(MORDRED)'] + 26.446247*dataset.loc[:, 'Mor13se:(MORDRED)'] + 53.579802*dataset.loc[:, 'Mor26m:(MORDRED)'] - 0.330472*dataset.loc[:, 'PEOE_VSA7:(MORDRED)'] - 1.235251*dataset.loc[:, 'SsOH:(MORDRED)'] + 3.458921*dataset.loc[:, 'PEOE_VSA5:(MORDRED)'] - 336.598009*dataset.loc[:, 'GATS1d:(MORDRED)'] + 64.284856*dataset.loc[:, 'AATSC4dv:(MORDRED)'] + 350.2463171947596

def smiles_visual(dataset):
  data = get_predict(dataset)
  mols = [Chem.MolFromSmiles(i) for i in dataset.loc[:, 'SMILES']]
  return (Draw.MolsToGridImage(mols, legends = ['Pred.inhibition = '+str(np.array(i).round(2))+'%' for i in data]))

st.title("QSAR prediction of inhibition of peroxidation oxidation")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)

st.image(smiles_visual(is_inEdge(uploaded_file)))
