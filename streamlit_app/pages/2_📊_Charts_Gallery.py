import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('streamlit_app/data/world_population.csv')
df['Growth Rate'] = round((df['Growth Rate'] - 1) * 100, 2)

st.title("World Population Analysis")
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# 2022 World Population Histogram
fig = px.histogram(df, x='2022 Population', title='2022 World Population Distribution', color_discrete_sequence=['#0C7BDC'])
fig.update_layout(
    xaxis_title_text='Population (Billions)',
    yaxis_title_text='Count',
)
col1.plotly_chart(fig, use_container_width=True)
col1.markdown(
    """
    What does the distribution of the world population look like?\n
    How to read this chart:
    - The x-axis represents the population in billions.
    - The y-axis represents the count of countries.
    Observations:
    - There are two outlier countries with populations between 1.4B-1.449B.
    - Most of the population lies between 0-49 million in 205 countries.
    - There are 27 countries that have a population between 50M-349M.
    """
)

# 2022 World Population Bar Chart
avg_growth = df.groupby('Continent')['Growth Rate'].mean().reset_index()
fig = px.bar(avg_growth, x='Continent', y='Growth Rate',
                   title='World Population Growth Rates Distribution')
fig.update_traces(marker_color='#0C7BDC')
col2.plotly_chart(fig, use_container_width=True)
col2.markdown(
    """
    What does the distribution of the world population growth look like?\n
    How to read this chart:
    - The x-axis represents continents.
    - The y-axis represents the average rate of growth.
    Observations:
    - Africa had the highest average population rate of growth.
    - Europe had the lowest average population rate of growth.
    - Africa and Europe could be an outliers since their averages are either greatly larger or smaller than all other continents.
    """
)

# Correlation Heatmap of Population
numeric_cols = ['2022 Population','2010 Population','1970 Population','Area (km²)',
        'Density (per km²)','Growth Rate','World Population Percentage']
df_numeric = df[numeric_cols]
corr = df_numeric.corr()
fig = px.imshow(corr, text_auto=True,
                title='Correlation Heatmap of Population')
col3.plotly_chart(fig, use_container_width=True)
col4.markdown(
    """
    What are the correlations netween different population metrics?\n
    How to read this chart:
    - White indicates a strong positive correlation.
    - Dark blue indicates a strong negative correlation.
    - Light blues indicate weak or no correlation.
    Observations:
    - Population and growth rate have strong negative correlation. 
    This means larger populations grow slower and smaller populations grow faster.
    - Population and population percentage have strong positive correlation.
    This means larger countries make up a larger portion of the whole population and
    smaller countries make up a smaller portion.
    - Area and density have a strong negative correlation.
    This means that larger countries tend to have lower population density while smaller countries tend to have higher population density.
    """
)

# 2022 World Population Choropleth Map
fig = go.Figure(data=go.Choropleth(
    locations = df['CCA3'],
    z = df['2022 Population'],
    text = (
        df['Country/Territory'] +
        "<br>Density (per km²): " + df['Density (per km²)'].astype('str') +
        "<br>Growth Rate: " + df["Growth Rate"].astype('str') + "%" +
        "<br>World Percentage: " + df['World Population Percentage'].astype('str') + "%"
    ),
    colorscale = 'Blues',
    colorbar_title = 'Population (Billions)',
))
fig.update_layout(title_text='2022 World Population')
st.plotly_chart(fig, use_container_width=True)
st.markdown(
    """
    What does the global distribution of population look like across different countries?\n
    How to read this map:
    - You can hover over any country to get information on it.
    - The darker blue the country the larger its population.
    Observations:
    - India and China both have populations over 1.4B.
    - Asia contains most of the world population.
    - Greenland has one of the smallest populations being 54.47k.
    - There are decline in growth in countries such as Japan being -0.53%.
    """
)
