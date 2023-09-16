import streamlit as st
import geocoder

api_key = st.secrets['WEATHER_API_KEY']
g = geocoder.ipinfo('me')

st.title('New Page')
st.write(g.city)
