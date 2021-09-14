from pandas._config.config import options
import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

@st.cache
def get_data(fileName):
    credit_app = pd.read_csv(fileName, header=None)
    return credit_app

with header:
    st.title("Welcome to my awesome project")

with dataset:
    st.header('Credit Approval Dataset')
    credit_app = get_data('Data/credit_approval.data')
    st.write(credit_app.head())
with features:
    st.header('Features selection')

with model_training:
    st.header('Model Training')
    st.text('This section the model is....')
    sel_col, disp_col = st.columns(2)

max_depth = sel_col.slider('What should be the max depth of the model?', min_value=10, max_value=100)
n_est = sel_col.selectbox('How many estimators should there be?', options=[100,200,300,'No limit'], index=0)
user_inp =  sel_col.text_input('Which feature should be input?', 'gender') 