#import packages
import streamlit as st
import pandas as pd
import plotly_express as px
from PIL import Image
from streamlit.commands.page_config import Layout

icon = Image.open('images/Favicon Transparent.ico')

st.set_page_config(page_title='Zillow Rental Index',
                   page_icon=icon,
                   layout='wide',
                   initial_sidebar_state="auto",
                   menu_items=None)

st.title('Rental Index')

# read dataset
rental_index = pd.read_csv('datasets/rent_index.csv')

# drop columns
rental_index.drop(columns=['RegionID', 'SizeRank', 'RegionType'], inplace=True)

# rename columns 
rental_index.rename(columns={'RegionName': 'region_name', 'StateName': 'state_name'}, inplace=True)

# fill for USA
rental_index.state_name.fillna('USA', inplace=True)

# state rental group
state_rental = rental_index.groupby('state_name').mean().T

#-------------------------------------------------------#

# National Rent

st.subheader('National Mean Rent')
st.write(px.line(state_rental, title='Mean Rent', template='plotly_white', height=900, width=1400, labels={'index': 'Date', 'value': 'Rent ($)'}))
st.title('')
#-------------------------------------------------------#

# Individual States

# filter the states
ga_rent = state_rental.GA
pa_rent = state_rental.PA   
md_rent = state_rental.MD
usa_rent = state_rental.USA

# combining filtered states
rents = pd.concat([ga_rent, pa_rent, md_rent, usa_rent], axis=1)

st.subheader('State Rent')
st.write(px.line(rents, title='Mean Rent', labels={'index':'Years', 'value':'Rent ($)'}, template='plotly_white', height=900, width=1400))
st.title('')
#---------------#

st.subheader('National Median Rent')

# filter for median 
state_rental_median = rental_index.groupby('state_name').median().T

# filter states 
ga_rent_median = state_rental_median.GA
pa_rent_median = state_rental_median.PA   
md_rent_median = state_rental_median.MD
usa_rent_median = state_rental_median.USA

# combine filters
rents_median = pd.concat([ga_rent_median, pa_rent_median, md_rent_median, usa_rent_median], axis=1)


st.write(px.line(state_rental_median, height=900, width=1400, labels={'index': 'Date', 'value': 'Rent ($)'}, title='Median Rent'))

st.write(px.line(rents_median, labels={'index':'Years', 'value':'Rent ($)'}, template='plotly_white', title='Median Rent', height=900, width=1400))

#--------------------------------------#

st.subheader('Year Over Year Change')
st.write(px.line(state_rental.pct_change(axis='rows')*100, title='Rent Percent Change Year Over Year, by State', 
                 template='plotly_white', labels={'index': 'Year', 'value':'Percent Change'}, height=900, width=1400))