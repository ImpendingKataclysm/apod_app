import streamlit as st

api_key = st.secrets['WEATHER_API_KEY']

st.title('New Page')
st.write(api_key)
