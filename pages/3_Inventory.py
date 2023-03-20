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

st.title('Home Invetory')

#------------------------------------------# 
# Dataset

inv = pd.read_csv('datasets\inventory.csv')
inv.drop(columns=['RegionID', 'SizeRank', 'RegionType'], inplace=True)
inv.rename(columns={'RegionName':'region_name', 'StateName':'state_name'}, inplace=True)
inv.state_name = inv.state_name.fillna('USA')

# Mean State inventory
st.subheader('State Inventory')

state_inv = inv.groupby('state_name').mean()

st.write(px.scatter(state_inv.loc[:,'1/31/2022':].mean(axis=1), log_y=True, title='Mean Inventory of Homes 2022', template='presentation', labels={'state_name': 'State', 'value':'Inventory'}, 
                    width=1400, height=900, color_discrete_sequence=['orange']))




#------------------------------------------# 
st.title('')
# Georgia
st.subheader('Georgia')
ga_inv = inv.query("state_name=='GA'").drop(columns='state_name')
pa_inv = inv.query("state_name=='PA'").drop(columns='state_name')
md_inv = inv.query("state_name=='MD'").drop(columns='state_name')

# filter relevant years
ga_inv_2018 = ga_inv.loc[:,'1/31/2018': '12/31/2018'].mean(axis=1)
ga_inv_2019 = ga_inv.loc[:,'1/31/2019': '12/31/2019'].mean(axis=1)
ga_inv_2020 = ga_inv.loc[:,'1/31/2020': '12/31/2020'].mean(axis=1)
ga_inv_2021 = ga_inv.loc[:,'1/31/2021': '12/31/2021'].mean(axis=1)
ga_inv_2022 = ga_inv.loc[:,'1/31/2022': '12/31/2022'].mean(axis=1)

# add region name
ga_inv_2018_full = pd.concat([ga_inv.region_name, ga_inv_2018], axis=1)
ga_inv_2019_full = pd.concat([ga_inv.region_name, ga_inv_2019], axis=1)
ga_inv_2020_full = pd.concat([ga_inv.region_name, ga_inv_2020], axis=1)
ga_inv_2021_full = pd.concat([ga_inv.region_name, ga_inv_2021], axis=1)
ga_inv_2022_full = pd.concat([ga_inv.region_name, ga_inv_2022], axis=1)

# rename column
ga_inv_2018_full.rename(columns={0:'Mean'}, inplace=True)
ga_inv_2019_full.rename(columns={0:'Mean'}, inplace=True)
ga_inv_2020_full.rename(columns={0:'Mean'}, inplace=True)
ga_inv_2021_full.rename(columns={0:'Mean'}, inplace=True)
ga_inv_2022_full.rename(columns={0:'Mean'}, inplace=True)

# merge years
merge1 = pd.concat([ga_inv_2018_full, ga_inv_2019], axis=1)
merge2 =pd.concat([merge1, ga_inv_2020], axis=1)
merge3 = pd.concat([merge2, ga_inv_2021], axis=1)
final_merge = pd.concat([merge3, ga_inv_2022], axis=1)


# final merge
final_merge.columns=['region_name','2018', '2019', '2020', '2021', '2022']

st.write(px.scatter(final_merge, x='region_name', y=['2018', '2019', '2020', '2021', '2022'], log_y=True, title='Georgia Mean Home Inventory', 
                    template='plotly_white', width=1400, height=900, labels={'region_name': 'City', 'value': 'Inventory'}))

st.write(px.box(final_merge, x='region_name', y=['2018', '2019', '2020', '2021', '2022'], log_y=True, title='Georgia Mean Home Inventory 2018-2022',
                template='plotly_white', width=1400, height=900, labels={'region_name': 'City', 'value': 'Inventory'}, color_discrete_sequence=['orange']))

#-------------#
st.title('')
# Pennsylvania
st.subheader('Pennsylvania')

# filter relevant years
pa_inv_2018 = pa_inv.loc[:,'1/31/2018': '12/31/2018'].mean(axis=1)
pa_inv_2019 = pa_inv.loc[:,'1/31/2019': '12/31/2019'].mean(axis=1)
pa_inv_2020 = pa_inv.loc[:,'1/31/2020': '12/31/2020'].mean(axis=1)
pa_inv_2021 = pa_inv.loc[:,'1/31/2021': '12/31/2021'].mean(axis=1)
pa_inv_2022 = pa_inv.loc[:,'1/31/2022': '12/31/2022'].mean(axis=1)

# add region name
pa_inv_2018_full = pd.concat([pa_inv.region_name, pa_inv_2018], axis=1)
pa_inv_2019_full = pd.concat([pa_inv.region_name, pa_inv_2019], axis=1)
pa_inv_2020_full = pd.concat([pa_inv.region_name, pa_inv_2020], axis=1)
pa_inv_2021_full = pd.concat([pa_inv.region_name, pa_inv_2021], axis=1)
pa_inv_2022_full = pd.concat([pa_inv.region_name, pa_inv_2022], axis=1)

# rename column
pa_inv_2018_full.rename(columns={0:'Mean'}, inplace=True)
pa_inv_2019_full.rename(columns={0:'Mean'}, inplace=True)
pa_inv_2020_full.rename(columns={0:'Mean'}, inplace=True)
pa_inv_2021_full.rename(columns={0:'Mean'}, inplace=True)
pa_inv_2022_full.rename(columns={0:'Mean'}, inplace=True)

# merge years
merge4 = pd.concat([pa_inv_2018_full, pa_inv_2019], axis=1)
merge5 =pd.concat([merge4, pa_inv_2020], axis=1)
merge6 = pd.concat([merge5, pa_inv_2021], axis=1)
final_merge2 = pd.concat([merge6, pa_inv_2022], axis=1)


# final merge
final_merge2.columns=['region_name','2018', '2019', '2020', '2021', '2022']

st.write(px.scatter(final_merge2, x='region_name', y=['2018', '2019', '2020', '2021', '2022'], log_y=True, title='Pennsylvania Mean Home Inventory', 
                    template='plotly_white', width=1400, height=900, labels={'region_name': 'City', 'value': 'Inventory'}))

st.write(px.box(final_merge2, x='region_name', y=['2018', '2019', '2020', '2021', '2022'], log_y=True, title='Pennsylvania Mean Home Inventory 2018-2022', 
                template='plotly_white', width=1400, height=900, labels={'region_name': 'City', 'value': 'Inventory'}, color_discrete_sequence=['orange']))

#--------------#
st.title('')
# Maryland
st.subheader('Maryland')

# filter relevant years
md_inv_2018 = md_inv.loc[:,'1/31/2018': '12/31/2018'].mean(axis=1)
md_inv_2019 = md_inv.loc[:,'1/31/2019': '12/31/2019'].mean(axis=1)
md_inv_2020 = md_inv.loc[:,'1/31/2020': '12/31/2020'].mean(axis=1)
md_inv_2021 = md_inv.loc[:,'1/31/2021': '12/31/2021'].mean(axis=1)
md_inv_2022 = md_inv.loc[:,'1/31/2022': '12/31/2022'].mean(axis=1)

# add region name
md_inv_2018_full = pd.concat([md_inv.region_name, md_inv_2018], axis=1)
md_inv_2019_full = pd.concat([md_inv.region_name, md_inv_2019], axis=1)
md_inv_2020_full = pd.concat([md_inv.region_name, md_inv_2020], axis=1)
md_inv_2021_full = pd.concat([md_inv.region_name, md_inv_2021], axis=1)
md_inv_2022_full = pd.concat([md_inv.region_name, md_inv_2022], axis=1)

# merge years
merge7 = pd.concat([md_inv_2018_full, md_inv_2019], axis=1)
merge8 =pd.concat([merge7, md_inv_2020], axis=1)
merge9 = pd.concat([merge8, md_inv_2021], axis=1)
final_merge3 = pd.concat([merge9, md_inv_2022], axis=1)


# final merge
final_merge3.columns=['region_name','2018', '2019', '2020', '2021', '2022']

st.write(px.scatter(final_merge3, x='region_name', y=['2018', '2019', '2020', '2021', '2022'], log_y=True, title='Maryland Mean Home Inventory', 
                    template='plotly_white', width=1400, height=900, labels={'region_name': 'City', 'value': 'Inventory'}))

st.write(px.box(final_merge3, x='region_name', y=['2018', '2019', '2020', '2021', '2022'], log_y=True, title='Maryland Mean Home Inventory', 
                template='plotly_white', width=1400, height=900, labels={'region_name': 'City', 'value': 'Inventory'}, color_discrete_sequence=['orange']))