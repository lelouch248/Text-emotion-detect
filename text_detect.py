import streamlit as st 
import joblib
model = joblib.load('model')
st.title('User emotion detection application backend [ working implementation]')
ip = st.text_input("Users message will be put here to predict the users emotion")
op = model.predict(ip)
if st.button('Analyse-emotion')
  st.title(op[0])

  
  
