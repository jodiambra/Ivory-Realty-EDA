#import packages
import streamlit as st
import pandas as pd
import plotly_express as px
from PIL import Image
from streamlit.commands.page_config import Layout

icon = Image.open('images/Favicon Transparent.ico')

st.set_page_config(page_title='Home Price Cuts',
                   page_icon=icon,
                   layout='wide',
                   initial_sidebar_state="auto",
                   menu_items=None)

st.title('Home Price Cuts')


#read dataframe
price_cuts = pd.read_csv('datasets/mean_price_cuts.csv')

#rename column
price_cuts.rename(columns={'RegionID':'region_id', 'SizeRank':'size_rank', 'RegionName':'region_name', 'RegionType':'region_type', 'StateName':'state_name'}, inplace=True)

# drop columns 
price_cuts.drop(columns=['region_id', 'size_rank', 'region_type'], inplace=True)

# fill for USA
price_cuts['state_name'].fillna('USA', inplace=True)

#-------------------------------------------#
# National Cuts
state_cuts = price_cuts.groupby('state_name').mean()

st.write(px.line(state_cuts.T, title='National Cuts', template='plotly_white', height=900, width=1200, labels={'index': 'Date', 'value':'Price Cut ($)'}))
st.title('')
#-------------------------------------------#
# Individual States

# state filters
ga_cuts = state_cuts.loc['GA']
pa_cuts = state_cuts.loc['PA']
md_cuts = state_cuts.loc['MD']

st.write(px.line(pd.concat([ga_cuts, pa_cuts, md_cuts], axis=1), title='Price Cuts', template='plotly_white', 
                 height=900, width=1200, labels={'index': 'Date', 'value':'Price Cut ($)'}))

st.title('')
#-------------------------------------------#

# Cities by state

# filter the states to get the cities
ga_city_cuts = price_cuts.query("state_name == 'GA'").drop(columns='state_name').reset_index(drop=True)
pa_city_cuts = price_cuts.query("state_name == 'PA'").drop(columns='state_name').reset_index(drop=True)
md_city_cuts = price_cuts.query("state_name == 'MD'").drop(columns='state_name').reset_index(drop=True)


st.subheader('Georgia')
st.write(px.line(ga_city_cuts.set_index('region_name').T, title='Price Cuts in Georgia', template='plotly_white', 
                 height=900, width=1200, labels={'index': 'Date', 'value':'Price Cut ($)'}))
st.title('')
#-------------#

st.subheader('Pennsylvania')
st.write(px.line(pa_city_cuts.set_index('region_name').T, title='Price Cuts in Pennsylvania', template='plotly_white', 
                 height=900, width=1200, labels={'index': 'Date', 'value':'Price Cut ($)'}))

st.title('')
#-------------#

st.subheader('Maryland')
st.write(px.line(md_city_cuts.set_index('region_name').T, title='Price Cuts in Maryland', template='plotly_white', 
                 height=900, width=1200, labels={'index': 'Date', 'value':'Price Cut ($)'}))