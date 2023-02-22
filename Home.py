#import packages
import streamlit as st
import pandas as pd
import plotly_express as px
from PIL import Image
from streamlit.commands.page_config import Layout


#----------------------------#
# Upgrade streamlit library
# pip install --upgrade streamlit

#-----------------------------#
# Page layout
icon = Image.open('images/Favicon Transparent.ico')

st.set_page_config(page_title='Ivory Realty Group EDA',
                   page_icon=icon,
                   layout='wide',
                   initial_sidebar_state="auto",
                   menu_items=None)
                
#-----------------------------#



st.title('IRG EDA')
    # Title Picture
 
image_1 = Image.open('images/LinkedIn Background Photo.png')

st.image(image_1, width=1300)

st.markdown('Welcome to Ivory Realty Group\'s exploratory data analysis on the current US housing market.')
st.markdown('Data is gathered from Zillow.')
st.markdown('This web application while highlight metrics of home value, forecasted home value, inventory, price cuts, and rental index.')

    #-------------------------------#

