import streamlit as st
from streamlit_multipage import MultiPage
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page

import pandas as pd
import numpy as np
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from streamlit_autorefresh import st_autorefresh
from sqlalchemy.sql import text
from sqlalchemy import *

from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from st_aggrid import AgGrid
from st_aggrid import GridOptionsBuilder,GridUpdateMode, DataReturnMode, JsCode
import streamlit.components.v1 as components

from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import smtplib
from os.path import basename
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from email.message import EmailMessage
from email.mime.application import MIMEApplication
import smtplib
from datetime import date
# %% Email Related module
import os

import streamlit_permalink as stp
import uuid
from st_clickable_images import clickable_images
from datetime import datetime
import pyodbc
# %%
st.set_page_config(layout="wide", page_title = 'IVY_1',initial_sidebar_state="collapsed")
st.markdown("<p style='text-align: center; color:#1428A0; font-size:40px; font-weight: bold; '>Salesman Account Change<br> Request Form 1</br></p>",unsafe_allow_html=True)
st.write("if you have any question, please contact IVY SOM team")
# %%

user = st.secrets['username']
pw = st.secrets['password']
host = 'DWPRO'
db = st.secrets['database']
engine = create_engine("mysql+pymysql://user:pw@host/db", pool_pre_ping=True)
conn = engine.connect()
conn.execute("SELECT * distinct(salesteam_text) from [[dbo]].[TEMPORARY]]] order by salesteam_text ascending;")
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()




# %% SalesTeam option 


# %%
colA,colB, colC , coldD, colE= st.columns([3,3,3,2,2])
with colE:
    main_p=st.button(label="Go Back To Main Page")
    st.markdown(""" <style>
div.stButton > button:first-child {
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
}</style>
""", unsafe_allow_html=True)
    if main_p:
        switch_page('Homepage')
    
# %%


serial_number = str(uuid.uuid4().fields[-1])[:12]
st.session_state.count = 0

cold1, cold2, cold3, cold4 = st.columns(4)
with cold1: 
    st.subheader('Serial Number')
    serialNumber = st.write(serial_number)
with cold2:
    st.subheader("Requester's Name")
    Requester = st.text_input(label = "Please write your name here", label_visibility='collapsed')
with cold3:
    st.subheader('Start Date')
    d1 = st.date_input(label = 'start date', label_visibility = 'collapsed')
with cold4:
    st.subheader('End Date')
    d2 = st.date_input(label = 'End Date',label_visibility='collapsed')

st.session_state['Serial Number'] = serial_number
st.session_state['Requester'] = Requester
col1, col2, col3 = st.columns([2,2,2])

with col1:
    st.markdown("<p style = 'text-align: center;background-color:aquamarine; color:black; font-size:30px; margin-top:30px;font-weight:bold;'>New Person</p>", unsafe_allow_html=True)

with col2:
    AT_1 = st.selectbox('Sales Team',options = df)
with col3:
    con = engine.connect()
    query2 = "select distinct(salesperson_text) from [[dbo]].[TEMPORARY]]] where salesdiv = 'div1' and salesteam_text = ?"
    df2 = con.execute(query2, AT_1)
    b = st.selectbox('Sales Man', options = df2)
col1_1,col1_2,col1_3 = st.columns(3)
with col1_1:
    st.markdown("<p style = 'text-align: center;background-color:aquamarine;color:black; font-size:30px; margin-top:30px;font-weight:bold;'>Current Person</p>", unsafe_allow_html=True)
with col1_2:

    c = st.selectbox('Sales Team', options = df, key = '2')
with col1_3:
    con = engine.connect()
    query3  = "select distinct(salesperson_text) from [[dbo]].[TEMPORARY]]] where salesdiv = 'div1' and salesteam_text = ?"
    df3 =con.execute(query3, c)
    d = st.selectbox('Sales Man', options = df3, key = '3')

# It's Applier's Form 

    
st.session_state['IVY Sales Team 1'] = c
new = ""
for i in st.session_state['IVY Sales Team 1']:
    new = ''.join(map(str,str(i)))
st.session_state['IVY Sales Team 1'] = new
st.session_state['IVY Sales Man 1'] = d



# %% Choosing Account
colA1, colA2 = st.columns(2)
with colA1:
    with engine.connect() as conn:
        query4 = """WITH T1 as(select a.*, b.shiptoparty_dba,b.address,b.state_key, b.city from [[dbo]].[TEMPORARY]]] a left join [ivy.mm.dim.shiptoparty] b 
        on a.shiptoparty = b.shiptoparty) select DISTINCT(T1.shiptoparty), T1.shiptoparty_dba, T1.address,T1.state_key, T1.city from T1 
        where T1.salesdiv = 'div1' and T1.salesperson_text = ?"""
        qry = conn.execute(query4, b)
        resultqry = []
        for row in qry:
            row_as_dict = row._mapping 
            row1 = row_as_dict.values()                                    
            resultqry.append(row1)
    st.markdown('#')
    st.text(' ')
    st.text(' ')
    st.header('Select Account')
    df2 = pd.DataFrame(list(resultqry), columns = ['Account Number','Account Name','Address','State','City'])
    gd = GridOptionsBuilder.from_dataframe(df2)
    gd.configure_pagination(enabled=True)
    getContextMenuItems = JsCode("""
function(e) {
        let api = e.api;        
        let sel = api.getSelectedRows();

        api.applyTransaction({remove: sel});
    };
""")
    grid_op = {
        "enableRangeSelection":True,
        "getContextMenuItems":getContextMenuItems,
    }
    gd.configure_grid_options(onRowSelected = grid_op)
    gd.configure_default_column(enablePivot = True, enableValue = True, enableRowGroup = True)
    gd.configure_selection(selection_mode = 'multiple', use_checkbox=True)
    gd.configure_side_bar()
    gd.configure_column("Account Number", headerCheckboxSelection = True)
    gdOptions = gd.build()
    
    grid_Table = AgGrid(df2, gridOptions=gdOptions,data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
                        update_mode = GridUpdateMode.SELECTION_CHANGED,
                        height = 1000,
                        allow_unsafe_jscode=True,
                        theme='balham',
                        width=0.5
                            )
    sel_row = grid_Table["selected_rows"]
    trows = len(sel_row)
    
with colA2:
    st.subheader(f'Total rows : {trows}')
    df = pd.DataFrame(sel_row, columns = ['Account Number','Account Name','State']) 
    st.header("Selected Account")  
    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_pagination(paginationAutoPageSize=True)
    gd.configure_default_column(editable=True, groupable=True,rowGroup = True)
    grid_op = {
        "enableRangeSelection":True,
        "getContextMenuItems":getContextMenuItems,
    }
    gd.configure_grid_options(onRowSelected = grid_op)
    grid_table2 = AgGrid(df,update_mode=GridUpdateMode.SELECTION_CHANGED,
                        height = 1000, allow_unsafe_jscode=True,width = 0.5,
                            theme='balham') 
   
    # %%
    # Create Result DataFrame to Send Email 
    num_row = len(df.index)
    df['From'] = str(d)
    df['To'] = str(b)
    df['Start_From'] = d1
    df['End_date'] = d2
    final = df[['From','To','Account Number','Account Name','State','Start_From','End_date']]
# %%
# Save File in Smartsheet Page 

# %%
    
# Submit button Form


