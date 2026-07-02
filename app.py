# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:34:07 2026
Goal: learning to run streamlit code for interactive dashboard in laptop browser
@author: Surendra
"""

#%% practice code (Gemini broswer): very first mock code to run interactive dashboard on computer browser

import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Interactive Data Dashboard")
df_choice = st.sidebar.selectbox("Select a Dataset", ["DF 1", "DF 2", "DF 3", "DF 4", "DF 5"])

# Generate a random dataset based on the sidebar selection
np.random.seed(int(df_choice[-1]))  # Keeps the random data consistent for each selection
random_data = np.random.randn(20, 2).cumsum(axis=0)

# Build the dataframe with standard 'Date' and 'Value' columns
date_range = pd.date_range(start="2026-01-01", periods=20, freq="D")
df = pd.DataFrame(random_data, index=date_range, columns=["Value A", "Value B"]).reset_index()
df.columns = ["Date", "Value A", "Value B"]

# Render the interactive chart and table
st.write(f"### Trend Plot for {df_choice}")
st.line_chart(data=df, x="Date", y=["Value A", "Value B"]) 
st.write("### Raw Data View", df)