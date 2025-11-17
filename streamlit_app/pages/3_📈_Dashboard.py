import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

df = pd.read_csv('streamlit_app/data/world_population.csv')

st.title("World Population Dashboard")

continents = st.multiselect('Select continents', df['Continent'].unique())

min_population, max_population = st.slider(
    "Select Population Range",
    df["2022 Population"].min(),
    df["2022 Population"].max(),
    (df["2022 Population"].min(), df["2022 Population"].max())
)

df_filtered = df[
    df["Continent"].isin(continents) &
    df["2022 Population"].between(min_population, max_population)
]

# 2022 World Population Bar Graph
fig = px.bar(
    df_filtered.groupby("Continent")["2022 Population"].sum().reset_index(),
    x="Continent",
    y="2022 Population",
    title="Total Population by Continent"
)
fig.update_traces(marker_color='#0C7BDC')
st.plotly_chart(fig, use_container_width=True)

# 2022 World Population Scatter Plot
fig = px.scatter(
    df_filtered,
    x="2022 Population",
    y="Growth Rate",
    color="Continent",
    hover_name="Country/Territory",
    title="Population vs Growth Rate"
)
st.plotly_chart(fig, use_container_width=True)

col1, col2, col3 = st.columns(3)
col1.metric("Countries Selected", len(df_filtered))
col2.metric("Average Growth Rate", f"{round(df_filtered['Growth Rate'].mean(), 2)}%")
col3.metric("Total Population", f"{df_filtered['2022 Population'].sum():,}")

st.markdown(
    """
    Insights:
    - Asia has the highest total population.
    - Africa has the highest growth rates.
    - Some limitations is not being able to see current year populations.
    """
)

st.markdown("World Population Dataset: https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset")
st.caption(f"Last refreshed: {datetime.now()}")
