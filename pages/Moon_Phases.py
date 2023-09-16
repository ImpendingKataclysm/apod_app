import datetime
import requests
import streamlit as st
import geocoder

api_key = st.secrets['WEATHER_API_KEY']
user_location = geocoder.ipinfo('me')
city = st.text_input('Enter your city')
region = st.text_input('Enter region (province, state, etc)')

if city and region:
    date = datetime.datetime.now().date()

    request_url = "https://api.weatherapi.com/v1/astronomy.json?" \
                  f"key={api_key}&q={city},{region}&dt={date}"
    response = requests.get(request_url)
    content = response.json()

    location = content['location']
    city = location['name']
    region = location['region']
    country = location['country']
    current_date = date.strftime('%B %d, %Y')

    astronomy = content['astronomy']['astro']
    moon_phase = astronomy['moon_phase']

    img_path_components = moon_phase.lower().split()
    img_path = '-'.join(img_path_components)

    st.title('Moon Phase')
    st.subheader(f'{city}, {region}, {country}')
    st.write(f'{current_date}')
    st.subheader(moon_phase)

    st.image(f'images/{img_path}.png')
else:
    st.write('Enter your location')
