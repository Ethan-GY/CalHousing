# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

# show the title
st.title('California Housing Data (1990) by Gao Yi')

# read csv
df = pd.read_csv('housing.csv')

# price slider
price_limit = st.slider(
    'Minimal Median House Price: ',
    0,
    500001,
    200000
)

st.write("See more filters in the sidebar:")

# sidebar
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique()
)

income_filter = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High')
)

# filter by income
if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
else:
    df = df[df.median_income > 4.5]

# filter by location
df = df[df.ocean_proximity.isin(location_filter)]

# filter by price
df = df[df.median_house_value >= price_limit]

# show the data on map
st.map(df)

# show the histogram
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(10, 5))
df.median_house_value.hist(ax=ax, bins=30)
st.pyplot(fig)

