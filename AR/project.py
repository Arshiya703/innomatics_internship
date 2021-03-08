import streamlit as st
import pandas as pd
from pickle import dump,load
st.markdown("<h1 style='text-align: center; color: black ;'>Feed Back</h1>", unsafe_allow_html=True)
st.markdown("<style>body{background-color:lightblue;},</style>", unsafe_allow_html=True)
st.sidebar.subheader("login")
username = st.sidebar.text_input("Username")
button_was_clicked = st.sidebar.button("submit")
col1=st.number_input("Enter your tenure from1 ")
col2=st.number_input("Enter your tenure from2 ")
classifier=load(open('pickel/cla.pkl','rb'))
prediction = classifier.predict([[col1,col2]])
click = st.button('SUBMIT')
if click:
    if prediction==1:
        st.write('output : 1 :smile:')
    else:
        st.write('Output : 0 :cry:')
