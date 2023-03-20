#import packages
import streamlit as st
import pandas as pd
import plotly_express as px
from PIL import Image
from streamlit.commands.page_config import Layout
from streamlit_folium import st_folium
from streamlit.components.v1 import components
import numpy as np


icon = Image.open('images/Favicon Transparent.ico')

st.set_page_config(page_title='Home Value Forecasting',
                   page_icon=icon,
                   layout='wide',
                   initial_sidebar_state="auto",
                   menu_items=None)

# Load dataset

hvf = pd.read_csv('datasets\home_value_forcast.csv')
hvf.drop(columns=['RegionID', 'RegionType'], inplace=True)
hvf.columns = ['size_rank', 'region', 'state',
               'base_date', 'feb', 'apr', 'jan_24']

#-------------------------------#

# grouping by state

state_sum = hvf.groupby('state')[['feb', 'apr', 'jan_24']].sum()
state_mean = hvf.groupby('state')[['feb', 'apr', 'jan_24']].mean()
state_feb = hvf.groupby('state')['feb'].sum()
state_apr = hvf.groupby('state')['apr'].sum()
state_jan = hvf.groupby('state')['jan_24'].sum()

#-------------------------#

# Home forecast table
st.title('Home Mean Forecasts')

st.subheader('Mean Home Value Predictions by State')
february = st.checkbox('Sort by February Predictions')
april = st.checkbox('Sort by April Predictions')
january = st.checkbox('Sort by January Predictions')

number = st.slider('Filter', min_value=5, max_value=50)

if february:
    st.table(state_mean.sort_values(by='feb', ascending=False).head(number))
elif april:
    st.table(state_mean.sort_values(by='apr', ascending=False).head(number))
elif january:
    st.table(state_mean.sort_values(by='jan_24', ascending=False).head(number))
else:
    st.table(state_mean.head(number))

with st.expander('Details'):
    st.write('Here, we see the month-ahead, quarter-ahead, and year-ahead forecast of Zillow\'s home value index.',
             'These forecasts are based on Zillow\'s Zestimate machine learning model. We see that Mississippi, Michigan, Arizona, and Kentucky are consistently',
             'in the top 5 states from February through April. Tennessee is in the top 5 states for April and January of next year. Interestingly, Georgia appears',
             'as the number 3 state in January Predictions. Positive denotes increase in value.')

#----------------------------#
# Mean value predictions
st.title('')
st.title('')

st.subheader('State Mean and Total Value Predictions')

sum = st.button('Get Total Values')
mean = st.button('Get Mean Values')
if sum:
    st.write(px.bar(state_sum, title='Total Values', labels={'state': 'State'},
                    template='plotly_white', orientation='v', height=900, width=1400))
elif mean:
    st.write(px.bar(state_mean, color_continuous_midpoint=['green'], title='Mean Values', labels={'state': 'State'},
                    template='plotly_dark', orientation='v', height=900, width=1400))
else:
    st.write(px.bar(state_mean, color_continuous_midpoint=['green'], title='Mean Values', labels={'state': 'State'},
                    template='plotly_dark', orientation='v', height=900, width=1400))

with st.expander('Details'):
    st.write('Here, we see the mean and total value predictions of each state. ')

#----------------------#

# box plot of forecasts

st.title('')
st.title('')
st.subheader('Distribution of Forecasts')
st.write(px.box(hvf, y=['feb', 'apr', 'jan_24'], title='Forecast Distributions',
         template='plotly_white', color_discrete_sequence=['green', 'orange', 'white'], height=900, width=1400))


#-----------------#
# state home value predictions
st.title('')
st.title('')

georgia = hvf.query("state== 'GA'")
penn = hvf.query("state== 'PA'")
maryl = hvf.query("state== 'MD'")

states = ['USA AVG', 'NY', 'CA', 'IL', 'TX', 'VA', 'FL', 'PA', 'GA', 'AZ', 'MA',
          'MI', 'WA', 'MN', 'CO', 'MO', 'MD', 'NC', 'OR', 'NV', 'OH', 'IN',
          'TN', 'RI', 'WI', 'OK', 'LA', 'KY', 'UT', 'CT', 'AL', 'HI', 'NE',
          'SC', 'NM', 'ID', 'AR', 'IA', 'KS', 'MS', 'ME', 'DE', 'NH', 'AK',
          'NJ', 'SD', 'WV', 'ND', 'VT', 'MT', 'WY']

states_sorted = sorted(states)

st.subheader('Home Value Predictions')

state = st.selectbox('Select State', states_sorted,
                     index=states_sorted.index('GA'))

st.write(px.scatter(hvf[hvf['state'] == state], y=['feb', 'apr', 'jan_24'], x='region',
         height=900, width=1400))


with st.expander('Details'):
    st.write('Here, we see the home value predictions filtered by state.')

#-----------------------------------#
# Regional Values 
st.title('')
st.title('')

# Georgia
st.subheader('State Regional Value Forcasts')
st.write(px.box(georgia, y=['feb', 'apr', 'jan_24'], x=georgia.region, title='Georgia',
        template='plotly_white', color_discrete_sequence=['green'], height=900, width=1400))

#----------------#
# Pennsylvania
st.write(px.box(penn, y=['feb', 'apr', 'jan_24'], x=penn.region, title='Pennsylvania',
        template='plotly_white', color_discrete_sequence=['green'], height=900, width=1400))

#----------------#
# Maryland

st.write(px.box(maryl, y=['feb', 'apr', 'jan_24'], x=maryl.region, title='Maryland',
        template='plotly_white', color_discrete_sequence=['green'], height=900, width=1400))

#------------------------------------------# 
st.title('')
html_string = "<div class='tableauPlaceholder' id='viz1679183574041' style='position: relative'><noscript><a href='#'><img alt='IRG Q1 2023 Home Value Forecast ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IR&#47;IRGHomeValueForcast&#47;Story1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='IRGHomeValueForcast&#47;Story1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IR&#47;IRGHomeValueForcast&#47;Story1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div><script type='text/javascript'>var divElement = document.getElementById('viz1679183574041');var vizElement = divElement.getElementsByTagName('object')[0];vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';var scriptElement = document.createElement('script');scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';vizElement.parentNode.insertBefore(scriptElement, vizElement);</script>"

st.components.v1.html(html_string, width=1400, height=1300, scrolling=True)
