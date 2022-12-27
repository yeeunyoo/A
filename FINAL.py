import streamlit as st
from streamlit_multipage import MultiPage
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx
import websockets
import asyncio
import pandas as pd
import numpy as np
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from streamlit_autorefresh import st_autorefresh
from sqlalchemy.sql import text
from sqlalchemy import *
import sqlite3
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from st_aggrid import AgGrid
from st_aggrid import GridOptionsBuilder,GridUpdateMode, DataReturnMode
import streamlit.components.v1 as components
from streamlit.web.server import Server

# %%
st.title('Your Request Has Been All Submitted! ')