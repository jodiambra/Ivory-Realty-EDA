#import packages
import streamlit as st
import pandas as pd
import plotly_express as px
from PIL import Image
from streamlit.commands.page_config import Layout

icon = Image.open('images/Favicon Transparent.ico')

st.set_page_config(page_title='Zillow Home Inventory',
                   page_icon=icon,
                   layout='wide',
                   initial_sidebar_state="auto",
                   menu_items=None)