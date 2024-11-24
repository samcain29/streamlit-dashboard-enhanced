import streamlit as st
import pandas as pd

st.header("2024 AHI 507 Streamlit Example")
st.subheader("We are going to go through a couple different examples of loading and visualization information into this dashboard")

st.text("""In this streamlit dashboard, we are going to focus on some recently released school learning modalities data from the NCES, for the years of 2021.""")

# ## https://healthdata.gov/National/School-Learning-Modalities-2020-2021/a8v3-a3m3/about_data
df = pd.read_csv("https://healthdata.gov/resource/a8v3-a3m3.csv?$limit=50000") ## first 1k 

## data cleaning 
df['week_recoded'] = pd.to_datetime(df['week'])
df['zip_code'] = df['zip_code'].astype(str)

df['week'].value_counts()

## box to show how many rows and columns of data we have: 
col1, col2, col3 = st.columns(3)
col1.metric("Columns", df.shape[1]) 
col2.metric("Rows", len(df))
col3.metric("Number of unique districts/schools:", df['district_name'].nunique())

## exposing first 1k of NCES 20-21 data
st.dataframe(df)



table = pd.pivot_table(df, values='student_count', index=['week'],
                       columns=['learning_modality'], aggfunc="sum")

table = table.reset_index()
table.columns

## line chart by week 
st.bar_chart(
    table,
    x="week",
    y="Hybrid",
)

st.bar_chart(
    table,
    x="week",
    y="In Person",
)

st.bar_chart(
    table,
    x="week",
    y="Remote",
)

# My Additions
import matplotlib.pyplot as plt
import streamlit as st

# Add descriptive text
st.markdown("## Dashboard Additions")

# Add a slider to filter data by week
import datetime

# Convert pandas Timestamp objects to Python datetime.date
min_date = df['week_recoded'].min().date()
max_date = df['week_recoded'].max().date()

# Create a slider to select a specific week
selected_date = st.slider(
    "Select a week to filter the data:",
    min_value=min_date,
    max_value=max_date,
    value=min_date,
    format="YYYY-MM-DD"
)

# Filter data based on the selected date
filtered_data = df[df['week_recoded'].dt.date == selected_date]

# Display the filtered data
st.markdown(f"### Data for the selected week: {selected_date}")
if not filtered_data.empty:
    st.dataframe(filtered_data)

    # Additional Visualization: Total students by learning modality for the selected week
    modality_counts = filtered_data.groupby('learning_modality')['student_count'].sum().reset_index()
    modality_counts.columns = ['Learning Modality', 'Student Count']

    # Create a bar chart for the selected week's learning modalities
    st.markdown("### Total Students by Learning Modality")
    st.bar_chart(modality_counts.set_index('Learning Modality'))
else:
    st.write("No data available for the selected week.")

