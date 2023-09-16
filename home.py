import streamlit as st

api_key = st.secrets['API_KEY']

st.subheader('Astronomy Picture of the Day')
st.write(api_key)
