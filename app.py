import streamlit as st
import pandas as pd

from vizualization import maps


about_markdown = """
Welcome to the Knox Beer Finder! 

Knoxville has experienced an explosion of amazing craft breweries in the past few years
 (we're coming for you Asheville). 
 
 I wanted a quick way to visualize all the breweries in our Scruffy City to make it 
 easier to explore all the craft beer Knoxville has to offer!
"""

st.set_page_config(
    page_title="Knox Beer Finder",
    page_icon="🍺",
    initial_sidebar_state="auto",
    layout="wide",
    menu_items={
        "About": about_markdown,
    },
)

st.title("Knox Beer Finder")
st.sidebar.title("About This App 🍺")
st.sidebar.write(about_markdown)


if st.button('Show me the beer!'):
    # Fetch the data
    breweries = pd.read_csv('./data/knox_breweries.csv')

    # MAP
    token_mapbox = st.secrets["mapbox_token"]
    st.markdown("## Local Breweries")
    st.plotly_chart(maps.map_plot(breweries, token_mapbox), use_container_width=True)

