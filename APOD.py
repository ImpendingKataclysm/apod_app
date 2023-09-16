import streamlit as st
import requests

api_key = st.secrets['API_KEY']
request_url = "https://api.nasa.gov/planetary/apod?" + \
              f"api_key={api_key}"

response = requests.get(request_url)
content = response.json()
title = content['title']
img_url = content['url']
img_response = requests.get(img_url)
page_text = content['explanation']
img_file = 'img.png'

with open(img_file, 'wb') as file:
    file.write(img_response.content)

st.title(title)
st.subheader('Astronomy Picture of the Day')
st.image(img_file)
st.write(page_text)
