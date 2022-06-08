import streamlit as st 
import joblib
model = joblib.load('model')
st.title('User emotion detection application backend [ working implementation]')
ip = st.text_input("Users message")
op = model.predict([ip])
if st.button("Analyse"):
  st.title(op[0])
  
