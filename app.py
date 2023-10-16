import streamlit as st
from about_page import show_about_page
from predict_page import show_predict_page
from explore_page import show_explore_page

st.title(":rainbow[Loan Apporval Prediction] 🤔")
st.markdown(''':red[Predict] :orange[and] :green[Explore] :blue[the] :violet[data] 🤟''')

aboutPage, predictPage, explorePage = st.tabs([":red[About]", ":green[Predict]", ":violet[Explore]"])

with aboutPage:
   show_about_page()

with predictPage:
   show_predict_page()

with explorePage:
   show_explore_page()