import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import plotly as px
import seaborn as sns
from time import sleep

col1,col2,col3=st.columns([0.25,0.5,0.25])
with col1:
   st.image("logo1.jpg")

with col2:
 st.title("D4H")
 st.subheader("Welcome to Data For Health")
 
with col3:
   st.image("logo2.jpg", width=150)

ABOUT="*D4H is a DHIS2 Sub-Module which forcuses on certain KPIs in the HIV/AIDS & TB - Care and Treatment Program.*"
if st.button("About D4H"):
   st.write(ABOUT)   

st.markdown ("---")

username=st.text_input("Username")
password=st.text_input("Password", type="password")

if st.button("Login"):
      if username=="admin" and password=="P@ssw0rd!":
       st.success("Logged in as  {}".format(username))
       st.write("Login Successful!")
       st.switch_page("pages/hts.py")
      else:
       st.error("Invalid Username or password. Please enter correct Login Credentials")
    


st.markdown ("---")
col1, col2,col3=st.columns([0.2,0.6,0.2])

with col2:
 st.image("Picture1.jpg", width=500)