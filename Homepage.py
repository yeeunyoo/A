import streamlit as st
from streamlit_multipage import MultiPage
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx
from streamlit.web.server import Server
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
import os
import IVY_1
import IVY_2
import IVY_3
st.set_page_config(
page_title="Account Change Request",
page_icon="🔎",
layout="wide",
initial_sidebar_state="collapsed",
)
colA, colB, colC, colD = st.columns([3,1,3,2])
with colC:
    st.markdown("""<input type="image" src="https://www.kissusa.com/media/logo/stores/1/kiss.png" width = "200px" height = "50px" />""", unsafe_allow_html=True)
st.markdown('#')
st.markdown("""<h1 style="font-size:50px; text-align: center; color:black; margin:10px;">Sales Account Change Request Form</h1>""", unsafe_allow_html=True)
for i in range(1, 7):
    st.markdown('#')
PAGES = {
    "IVY_1":IVY_1,
    "IVY_2" :IVY_2
}


beta1, beta2 = st.columns(2)
with beta1:
    IVY = st.button("IVY")
    if IVY:
        switch_page('IVY_1')
with beta2:
    RED = st.button('RED')
    if RED:
        switch_page('RED 01')

    
st.markdown("""<style>
 .element-container:nth-of-type(3) button {
      background-color: #ce1126;
    color: white;
    height: 3em;
    width: 12em;
    border-radius:10px;
    border:3px solid #000000;
    font-size:20px;
    font-weight: bold;
    margin: auto;
    display: block;
            height: 3em;
}</style>""",unsafe_allow_html=True)


import streamlit as st
import pyodbc

# Initialize connection.
# Uses st.experimental_singleton to only run once.
server = st.secrets['server']
database = st.secrets['database']
username = st.secrets['username']
password = st.secrets['password']
connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)

