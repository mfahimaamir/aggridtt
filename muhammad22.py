from collections import defaultdict
from matplotlib.cm import get_cmap
from pivottablejs import pivot_ui
from st_aggrid import AgGrid
import pandas as pd

from st_aggrid import AgGrid
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, ColumnsAutoSizeMode
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid import JsCode, AgGrid, GridOptionsBuilder
from st_aggrid.shared import ColumnsAutoSizeMode
from st_aggrid.shared import GridUpdateMode
import altair as alt ##https://altair-viz.github.io/
import datetime
import matplotlib
import matplotlib as mb
import matplotlib.pyplot as plt
import mysql.connector
import numpy
import numpy as np
import os
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st
import streamlit.components.v1 as components
matplotlib.use('Agg') #서버에서, 화면에 표시하기 위해서 필요









st.html("""
    <style>
        .stMainBlockContainer {
            max-width:350rem;
            max-hight:10rem;
        }
    </style>
    """
)

    
data = {
    'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 'Asia', 'Asia'],
    'Country': ['USA', 'USA', 'Canada', 'Germany', 'France', 'Japan', 'China'],
    'City': ['New York', 'Los Angeles', 'Toronto', 'Berlin', 'Paris', 'Tokyo', 'Beijing']
    }

df = pd.DataFrame(data)


#df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(df)