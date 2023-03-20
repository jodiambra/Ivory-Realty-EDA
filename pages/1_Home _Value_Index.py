#import packages
import streamlit as st
import pandas as pd
import plotly_express as px
from PIL import Image
from streamlit.commands.page_config import Layout
import numpy as np
from streamlit.components.v1 import components

icon = Image.open('images/Favicon Transparent.ico')

st.set_page_config(page_title='Home Value Index',
                   page_icon=icon,
                   layout='wide',
                   initial_sidebar_state="auto",
                   menu_items=None)


hvi = pd.read_csv('datasets/home_value_index.csv')
hvi.drop(columns=['RegionID', 'SizeRank', 'RegionType'], inplace=True)
hvi.rename(columns={'RegionName': 'region_name', 'StateName':'state_name'}, inplace=True)


#-----------------------------------------------------------------------------------------#
st.title('Zillow Home Value Index')

#-----------------------------------------------------------------------------------------#

# Across the US 

yr_2000 = ['1/31/2000', '2/29/2000', '3/31/2000', '4/30/2000', '5/31/2000', '6/30/2000', '7/31/2000', '8/31/2000', '9/30/2000', '10/31/2000', '11/30/2000', '12/31/2022']

# Generate list names
list_names = ['yr_' + str(i) for i in range(2000, 2023)]

# Create empty lists
for name in list_names:
    globals()[name] = []

# Populate lists
for i in range(1, 13):
    for name in list_names:
        if int(name[3:]) == 2022 and i > 12:
            break
        date_str = str(i) + '/1/' + name[3:]
        dt = pd.to_datetime(date_str)
        last_day = str(dt.to_period('M').to_timestamp('M').date())
        globals()[name].append(last_day)

hvi_state_mean = hvi.groupby('state_name').mean()

st_avg_2000 = hvi_state_mean.iloc[:, :12]
st_avg_2001 = hvi_state_mean.iloc[:, 12:24]
st_avg_2002 = hvi_state_mean.iloc[:, 24:36]
st_avg_2003 = hvi_state_mean.iloc[:, 36:48]
st_avg_2004 = hvi_state_mean.iloc[:, 48:60]
st_avg_2005 = hvi_state_mean.iloc[:, 60:72]
st_avg_2006 = hvi_state_mean.iloc[:, 72:84]
st_avg_2007 = hvi_state_mean.iloc[:, 84:96]
st_avg_2008 = hvi_state_mean.iloc[:, 96:108]
st_avg_2009 = hvi_state_mean.iloc[:, 108:120]
st_avg_2010 = hvi_state_mean.iloc[:, 120:132]
st_avg_2011 = hvi_state_mean.iloc[:, 132:144]
st_avg_2012 = hvi_state_mean.iloc[:, 144:156]
st_avg_2013 = hvi_state_mean.iloc[:, 156:168]
st_avg_2014 = hvi_state_mean.iloc[:, 168:180]
st_avg_2015 = hvi_state_mean.iloc[:, 180:192]
st_avg_2016 = hvi_state_mean.iloc[:, 192:204]
st_avg_2017 = hvi_state_mean.iloc[:, 204:216]
st_avg_2018 = hvi_state_mean.iloc[:, 216:228]
st_avg_2019 = hvi_state_mean.iloc[:, 228:240]
st_avg_2020 = hvi_state_mean.iloc[:, 240:252]
st_avg_2021 = hvi_state_mean.iloc[:, 252:264]
st_avg_2022 = hvi_state_mean.iloc[:, 264:276]

# state names
state_names = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 
'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 
'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']


# means of each state for the year
mean_2000 = st_avg_2000.mean(axis=1)
mean_2001 = st_avg_2001.mean(axis=1)
mean_2002 = st_avg_2002.mean(axis=1)
mean_2003 = st_avg_2003.mean(axis=1)
mean_2004 = st_avg_2004.mean(axis=1)
mean_2005 = st_avg_2005.mean(axis=1)
mean_2006 = st_avg_2006.mean(axis=1)
mean_2007 = st_avg_2007.mean(axis=1)
mean_2008 = st_avg_2008.mean(axis=1)
mean_2009 = st_avg_2009.mean(axis=1)
mean_2010 = st_avg_2010.mean(axis=1)
mean_2011 = st_avg_2011.mean(axis=1)
mean_2012 = st_avg_2012.mean(axis=1)
mean_2013 = st_avg_2013.mean(axis=1)
mean_2014 = st_avg_2014.mean(axis=1)
mean_2015 = st_avg_2015.mean(axis=1)
mean_2016 = st_avg_2016.mean(axis=1)
mean_2017 = st_avg_2017.mean(axis=1)
mean_2018 = st_avg_2018.mean(axis=1)
mean_2019 = st_avg_2019.mean(axis=1)
mean_2020 = st_avg_2020.mean(axis=1)
mean_2021 = st_avg_2021.mean(axis=1)
mean_2022 = st_avg_2022.mean(axis=1)



#-------------# 
st.subheader('Average Home Values Across the US')
fig = px.scatter(y=[mean_2018, mean_2019, mean_2020, mean_2021, mean_2022 ], x= state_names, labels={'x': 'States', 'value':'Home Values'}, title='Mean Home Values from 2018-2022', height=900, width=1400)
series_names = ["2018", "2019", "2020", "2021", "2022"]

for idx, name in enumerate(series_names):
    fig.data[idx].name = name
    fig.data[idx].hovertemplate = name

st.write(fig)

#-------------# 

st.write(px.box(y=[mean_2018, mean_2019, mean_2020, mean_2021, mean_2022 ], x= state_names, labels={'x': 'States', 'value':'Home Values'}, 
                height=900, width=1400,  title='Mean Home Value Distribution from 2018-2022', color_discrete_sequence=['green']))

st.title('')
#-------------# 
       
st.write(px.scatter(st_avg_2022.mean(axis=1), title='Average Home Values in 2022', labels={'state_name':'States'}, template='plotly_white', height=900, width=1400,
                     size=st_avg_2022.mean(axis=1), color=st_avg_2022.index))

st.title('')
#---------------------------------------------#



#---------------------------------------------#

# Georgia
st.subheader('Georgia')
ga = hvi.query("state_name=='GA'")
ga.set_index('region_name', inplace=True)

ga.drop(columns='state_name', inplace=True)

ga_2018 = ga.loc[:,'1/31/2018':'12/31/2018'].mean(axis=1)
ga_2019 = ga.loc[:,'1/31/2019':'12/31/2019'].mean(axis=1)
ga_2020 = ga.loc[:,'1/31/2020':'12/31/2020'].mean(axis=1)
ga_2021 = ga.loc[:,'1/31/2021':'12/31/2021'].mean(axis=1)
ga_2022 = ga.loc[:,'1/31/2022':'12/31/2022'].mean(axis=1)

#-------------# 

fig = px.scatter(y=[ga_2018, ga_2019, ga_2020, ga_2021, ga_2022], x=ga_2018.index, title='Mean Georgia Home Value from 2018-2022', labels={'x':'City'}, 
                 height=900, width=1400)
series_names = ["2018", "2019", "2020", "2021", "2022"]

for idx, name in enumerate(series_names):
    fig.data[idx].name = name
    fig.data[idx].hovertemplate = name

st.write(fig)

#-------------# 

st.write(px.box(y=[ga_2018, ga_2019, ga_2020, ga_2021, ga_2022], x=ga_2018.index, title='Mean Georgia Home Value from 2018-2022', height=900, width=1400, 
                color_discrete_sequence=['orange']))

#-----------------------------------------------------------------------------------------#

# Pennsylvania
st.title('')
st.title('')
st.subheader('Pennsylvania')

pa = hvi.query("state_name=='PA'")
pa.set_index('region_name', inplace=True)

pa_2018 = pa.loc[:,'1/31/2018':'12/31/2018'].mean(axis=1)
pa_2019 = pa.loc[:,'1/31/2019':'12/31/2019'].mean(axis=1)
pa_2020 = pa.loc[:,'1/31/2020':'12/31/2020'].mean(axis=1)
pa_2021 = pa.loc[:,'1/31/2021':'12/31/2021'].mean(axis=1)
pa_2022 = pa.loc[:,'1/31/2022':'12/31/2022'].mean(axis=1)

#-------------# 

fig = px.scatter(y=[pa_2018, pa_2019, pa_2020, pa_2021, pa_2022], x=pa_2018.index, title='Mean Pennsylvania Home Value from 2018-2022', labels={'x':'City'}, height=900, width=1400
)
series_names = ["2018", "2019", "2020", "2021", "2022"]

for idx, name in enumerate(series_names):
    fig.data[idx].name = name
    fig.data[idx].hovertemplate = name

st.write(fig)

#-------------# 

st.write(px.box(y=[pa_2018, pa_2019, pa_2020, pa_2021, pa_2022], x=pa_2018.index, title='Mean Pennsylvania Home Value from 2018-2022', labels={'x':'City'}, 
                height=900, width=1400, color_discrete_sequence=['orange']))

#-----------------------------------------------------------------------------------------#

# Maryland

st.title('')
st.title('')
st.subheader('Maryland')

md = hvi.query("state_name=='MD'")
md.set_index('region_name', inplace=True)
md.drop(columns='state_name', inplace=True)

md_2018 = md.loc[:,'1/31/2018':'12/31/2018'].mean(axis=1)
md_2019 = md.loc[:,'1/31/2019':'12/31/2019'].mean(axis=1)
md_2020 = md.loc[:,'1/31/2020':'12/31/2020'].mean(axis=1)
md_2021 = md.loc[:,'1/31/2021':'12/31/2021'].mean(axis=1)
md_2022 = md.loc[:,'1/31/2022':'12/31/2022'].mean(axis=1)

#-------------# 

fig = px.scatter(y=[md_2018, md_2019, md_2020, md_2021, md_2022], x=md_2018.index, title='Mean Maryland Home Value from 2018-2022', labels={'x':'City'}, height=900, width=1400
)
series_names = ["2018", "2019", "2020", "2021", "2022"]

for idx, name in enumerate(series_names):
    fig.data[idx].name = name
    fig.data[idx].hovertemplate = name

st.write(fig)

#-------------# 

st.write(px.box(y=[md_2018, md_2019, md_2020, md_2021, md_2022], x=md_2018.index, title='Mean Maryland Home Value from 2018-2022', labels={'x':'City'}, 
                height=900, width=1400, color_discrete_sequence=['orange']))

#-----------------------------------------------------------------------------------------#


html_string = "<div class='tableauPlaceholder' id='viz1679333742348' style='position: relative'><noscript><a href='#'><img alt='IRG Home Value Index ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IR&#47;IRGHomeValueIndex&#47;Story1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='IRGHomeValueIndex&#47;Story1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IR&#47;IRGHomeValueIndex&#47;Story1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1679333742348');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"

st.components.v1.html(html_string, width=1400, height=1300, scrolling=True)