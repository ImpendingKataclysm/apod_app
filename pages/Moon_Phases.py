import datetime
import requests
import streamlit as st
import geocoder

api_key = st.secrets['WEATHER_API_KEY']
user_location = geocoder.ipinfo('me')
city = user_location.city
date = datetime.datetime.now().date()
current_date = date.strftime('%B %d, %Y')

request_url = "https://api.weatherapi.com/v1/astronomy.json?" \
              f"key={api_key}&q={city}&dt={date}"
response = requests.get(request_url)
content = response.json()

astronomy = content['astronomy']['astro']
moon_phase = astronomy['moon_phase']

img_path_components = moon_phase.lower().split()
img_path = '-'.join(img_path_components)

st.title('Moon Phase')
st.subheader(f'{current_date}')
st.subheader(moon_phase)

st.image(f'images/{img_path}.png')
