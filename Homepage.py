import streamlit as st
from streamlit_multipage import MultiPage
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx
from streamlit.web.server import Server
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
import os
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
@st.experimental_singleton
def init_connection():
    connection = pyodbc.connect(
    driver = "ODBC Driver 17 for SQL Server",
    server = os.environ[st.secrets["server"]],
    database = os.environ[st.secrets['database']], 
    uid = os.environ[st.secrets['username']],
    pwd = os.environ[st.secrets['password']])
    return connection

conn = init_connection()
# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from [ivy.mm.dim.sales_master];")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
