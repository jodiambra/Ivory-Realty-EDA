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

st.markdown('For investors, this data provides valuable insights into the current and projected state of the US housing market. By utilizing this platform, ')
st.markdown('investors can make informed decisions about where to allocate their resources and capitalize on potential investment opportunities. Whether ')
st.markdown('you\'re a seasoned real estate investor or new to the market, the Ivory Realty Group\'s exploratory data analysis can provide you with the')
st.markdown('information you need to make smart investments in the US housing market. So why wait? Start exploring today and take your first step towards')
st.markdown(' building a profitable real estate portfolio!')

#-------------------------------#

