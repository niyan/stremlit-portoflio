import pandas as pd
import numpy as np
import streamlit as st
from datetime import date
import db
from db import conn

def say_hello():
    st.write('fuck johnson')
    return 

sheet_url = 'https://docs.google.com/spreadsheets/d/1k6Qb9vYyB0zPp8c13gg7YmXa8qE5r2JQjQkiPjwbzMI/edit#gid=1560465419'
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

df = pd.read_csv(url_1)

df = df[['Symbol', 'Token', 'Exchange', 'Quantity', 'Cost']]

if st.button('Say hello'):
     st.write('Why hello there')
else:
    #with st.container():
    #    st.write(df)
    say_hello()


