#import packages
import streamlit as st
import pandas as pd
import plotly_express as px
from PIL import Image
from streamlit.commands.page_config import Layout
from streamlit_folium import st_folium



import folium
from folium import plugins
import ipywidgets
import geocoder
import geopy
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

st.title('')

st.title('')


st.subheader('State Mean and Total Value Predictions')

sum = st.button('Get Total Values')
mean = st.button('Get Mean Values')
if sum:
    st.write(px.bar(state_sum, title='Total Values', labels={'state': 'State'},
                    template='plotly_white', orientation='v', height=900, width=1400))
elif mean:
    st.write(px.bar(state_mean, color_discrete_sequence=['green', 'lightgreen', 'white'], title='Mean Values', labels={'state': 'State'},
                    template='plotly_dark', orientation='v', height=900, width=1400))
else:
    st.write(px.bar(state_mean, color_discrete_sequence=['green', 'lightgreen', 'white'], title='Mean Values', labels={'state': 'State'},
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

st.title('')
st.title('')
st.subheader('State Regional Value Forcasts')
st.write(px.box(georgia, y=['feb', 'apr', 'jan_24'], x=georgia.region, title='Georgia',
        template='plotly_white', color_discrete_sequence=['green', 'orange', 'white'], height=900, width=1400))

# Georgia Regional map

# multiple markers using dictionary jan_24 predictions
markers_dict = {'Atlanta, 1.3': [33.7490, -84.3880],
        'Augusta, 1.6': [33.4735, -82.0101],
        'Savannah, 2.8': [32.0809, -81.0912],
        'Columbus, 0.3': [32.4600, -84.9877],
        'Macon, 3.4': [32.8407, -83.6324],
        'Athens, 3.4': [33.9609, -83.3779],
        'Gainesville, 1.8': [34.2979, -83.8241],
        'Warner Robins, 1.1': [32.6130, -83.6242],
        'Valdosta, 2.0': [30.8327, -83.2785],
        'Albany, 2.0': [31.5785, -84.1557],
        'Dalton, 2.8': [34.7698, -84.9702],
        'Brunswick, 2.3': [31.1499, -81.4915],
        'LaGrange, 2.0': [33.0363, -85.0319],
        'Rome, 4.8': [34.2570, -85.1647],
        'Hinesville, 1.8': [31.8469, -81.5960],
        'Statesboro, 1.2': [32.4487, -81.7832],
        'Jefferson, 2.7': [34.1283, -83.6023],
        'Dublin, 3.1': [32.5404, -82.9038],
        'Calhoun, 3.1': [34.5034, -84.9427],
        'St. Marys, 0.7': [30.7563, -81.5729],
        'Waycross, 4.6': [31.2134, -82.3549],
        'Milledgeville, 3.6': [33.0801, -83.2321],
        'Douglas, 2.3': [31.5095, -82.8506],
        'Cornelia, 2.3': [34.5116, -83.5282],
        'Moultrie, 2.4': [31.1795, -83.7895],
        'Thomasville, 1.7': [30.8375, -83.9787],
        'Cedartown, 5.8 ': [34.0141, -85.2514],
        'Tifton, 0.3': [31.4505, -83.5086],
        'Vidalia, 2.8': [32.2177, -82.4128],
        'Americus, 0.6': [32.0724, -84.2329],
        'Jesup, 5.1': [31.6078, -81.8851],
        'Thomaston, 6.9': [32.8889, -84.3266],
        'Bainbridge, 4.4': [30.9034, -84.5820],
        'Toccoa, 6.0': [34.5793, -83.3326],
        'Summerville, 10.2': [34.4813, -85.3489],
        'Cordele, 0.6': [31.9635, -83.7820],
        'Fitzgerald, 2.1': [31.7174, -83.2527]
        }

# create map
map_cities = folium.Map(location=[33, -84], zoom_start=7, width=1200, height=900, control_scale=True)

# plot locations
for i in markers_dict.items():
    folium.Marker(location=i[1], popup=i[0], icon=folium.Icon(color='green', icon='car', prefix='fa')
    ).add_to(map_cities)

# measure control
measure_control = plugins.MeasureControl(position='topleft', active_color='blue', completed_color='green', primary_length_unit='miles')

# add measure control to map
map_cities.add_child(measure_control)
# display map
st_folium(map_cities, width=800)




st.write(px.box(penn, y=['feb', 'apr', 'jan_24'], x=penn.region, title='Pennsylvania',
        template='plotly_white', color_discrete_sequence=['orange', 'orange', 'white'], height=900, width=1400))


# multiple markers using dictionary jan_24 predictions
markers_dict = {
'Philadelphia, -0.2': [39.9526, -75.1652], 
'Pittsburgh, -0.6': [40.4406, -79.9959], 
'Allentown, 0.8': [40.6084, -75.4902], 
'Harrisburg, -0.9': [40.2732, -76.8867], 
'Scranton, 3.0': [41.4080, -75.6624], 
'Lancaster, -0.3': [40.0379, -76.3055], 
'York, -1.2': [39.9626, -76.7277], 
'Reading, 0.7': [40.3356, -75.9277], 
'Erie, -0.8': [42.1292, -80.0851], 
'East Stroudsburg, 4.6': [41.0028, -75.1773], 
'State College, -1.7': [40.7934, -77.8600], 
'Chambersburg, 0.0': [39.9376, -77.6611], 
'Lebanon, -0.4': [40.3409, -76.4112], 
'Pottsville, 5.3': [40.6857, -76.1955], 
'Johnstown, 3.3': [40.3276, -78.9222], 
'Altoona, -1.9': [40.5187, -78.3947], 
'Williamsport, -2.9': [41.2412, -77.0011], 
'Gettysburg, -0.8': [39.8309, -77.2311], 
'Sunbury, 4.2': [40.8626, -76.7944], 
'New Castle, 1.4': [41.0037, -80.3470], 
'Meadville, 1.2': [41.6414, -80.1514], 
'Indiana, -2.0': [40.6215, -79.1528], 
'Bloomsburg, -0.6': [41.0047, -76.4549], 
'DuBois, 3.2': [41.1197, -78.7626], 
'Somerset, 0.8': [40.0054, -79.0781], 
'Sayre, -3.2': [41.9786, -76.5157], 
'Oil City, 0.9': [41.4309, -79.7076], 
'Lewistown, 2.8': [40.5993, -77.5712], 
'Huntingdon, -0.4': [40.4842, -78.0100], 
'Lewisburg, -1.1': [40.9645, -76.8844], 
'Bradford, 1.1': [41.9562, -78.6478], 
'Selinsgrove, 0.4': [40.7982, -76.8622], 
'Warren, -1.6': [41.8435, -79.1448], 
'Lock Haven, -3.0': [41.1373, -77.4469]}

# create map
map_cities2 = folium.Map(location=[41, -77], zoom_start=7, width=1200, height=900, control_scale=True)

# plot locations
for i in markers_dict.items():
    folium.Marker(location=i[1], popup=i[0], icon=folium.Icon(color='green', icon='car', prefix='fa')
    ).add_to(map_cities2)

# measure control
measure_control = plugins.MeasureControl(position='topleft', active_color='blue', completed_color='green', primary_length_unit='miles')

# add measure control to map
map_cities2.add_child(measure_control)
# display map
st_folium(map_cities2, width=800)


st.write(px.box(maryl, y=['feb', 'apr', 'jan_24'], x=maryl.region, title='Maryland',
        template='plotly_white', color_discrete_sequence=['forestgreen', 'orange', 'white'], height=900, width=1400))

# multiple markers using dictionary jan_24 predictions
markers_dict = {
    'Baltimore, -1.6': [39.2904, -76.6122],
    'Hagerstown, 0.5': [39.6418, -77.7200],
    'California, -1.9': [38.3001, -76.5075],
    'Cumberland, 1.8': [39.6528, -78.7625],
    'Easton, -1.4': [38.7745, -76.0768],
    'Cambridge, 2.3': [38.5633, -76.0768]
}

# create map
map_cities3 = folium.Map(location=[39, -76.6], zoom_start=7, width=1200, height=900, control_scale=True)

# plot locations
for i in markers_dict.items():
    folium.Marker(location=i[1], popup=i[0], icon=folium.Icon(color='green', icon='car', prefix='fa')
    ).add_to(map_cities3)

# measure control
measure_control = plugins.MeasureControl(position='topleft', active_color='blue', completed_color='green', primary_length_unit='miles')

# add measure control to map
map_cities3.add_child(measure_control)
# display map
st_folium(map_cities3, width=800)

#------------------------------------------# 

