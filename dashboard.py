# dashboard.py
import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("logs.db")
df = pd.read_sql_query("SELECT * FROM logs ORDER BY timestamp DESC", conn)
st.set_page_config(
    page_title="System Logs Dashboard",  
    page_icon="🧠",                      
    layout="wide",                       
    initial_sidebar_state="expanded"     
)
st.title("System Logs Dashboard")
st.dataframe(df)

