import streamlit as st

st.set_page_config(
    page_title="Tablero de Lotes y Cultivos",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Aplicacion de prueba 123")

with st.sidebar:
    st.title("sidebar")


import pandas as pd 

data = pd.read_csv('csv_rindes.csv')

st.data_editor(data)

import geopandas as gpd
from shapely import wkt

def generate_gdf(df, geometry='centroid'):
    df['geometry'] = df[geometry].apply(wkt.loads)
    gdf = gpd.GeoDataFrame(df, geometry='geometry')
    return gdf

gdf = generate_gdf(data)

st.session_state.gdf = gdf