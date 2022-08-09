import plotly.express as px
import streamlit as st


@st.cache
def map_plot(df, token_mapbox):
    px.set_mapbox_access_token(token_mapbox)
    fig = px.scatter_mapbox(
        df,
        hover_data=["id"],
        hover_name="name",
        zoom=12,
        lat="latitude",
        lon="longitude",
    )
    fig.update_layout(autosize=True, hovermode="closest", height=800)

    return fig
