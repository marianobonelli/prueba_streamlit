import folium
from streamlit_folium import st_folium
import streamlit as st


gdf = st.session_state.gdf

# Assuming gdf is your GeoDataFrame with a 'geometry' column containing Point geometries
m = folium.Map(location=[gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()], zoom_start=7)

# Loop through each row in the GeoDataFrame
for index, row in gdf.iterrows():
    # Extract the point coordinates from the geometry
    point = row['geometry']
    # Add a CircleMarker for each point
    folium.CircleMarker(location=(point.y, point.x)).add_to(m)

# Display the map in a Streamlit app
st_folium(m, use_container_width=True)