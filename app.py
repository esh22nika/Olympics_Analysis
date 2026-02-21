import streamlit as st
import pandas as pd
import preprocessor
import helper

df=pd.read_csv('noc_regions.csv')
region_df=pd.read_csv('athlete_events.csv')

df=preprocessor.preprocess(df)

st.title("Olympics Data Analysis")
st.sidebar.title("Olympics Data Analysis")
user_menu=st.sidebar.radio("Select an option", ("Medal Tally", "Overall Analysis", "Country-wise Analysis", "Athlete-wise Analysis"))

st.dataframe(df)

if user_menu=="Medal Tally":
    medal_tally=helper.medal_tally(df)
    st.dataframe(medal_tally)
