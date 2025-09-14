import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("metadata.csv")

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Filter by year
year_range = st.slider("Select year range", 2015, 2023, (2020, 2021))
filtered = df[(pd.to_datetime(df['publish_time'], errors='coerce').dt.year >= year_range[0]) &
              (pd.to_datetime(df['publish_time'], errors='coerce').dt.year <= year_range[1])]

st.write("Data Sample", filtered.head())

# Plot
fig, ax = plt.subplots()
filtered['publish_time'] = pd.to_datetime(filtered['publish_time'], errors='coerce')
filtered['year'] = filtered['publish_time'].dt.year
filtered['year'].value_counts().sort_index().plot(kind='bar', ax=ax)
st.pyplot(fig)
