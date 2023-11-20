import streamlit as st
import pandas as pd
import altair as alt
import time


df = pd.read_csv('Midterm Data.csv', sep=',')

st.dataframe(df)