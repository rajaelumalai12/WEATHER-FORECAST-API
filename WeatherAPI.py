import streamlit as st
import requests
st.title("Weather App ☀️")
st.markdown("""
<style>
    .stApp{background-color: #F2F27A;}
</style>
""", unsafe_allow_html=True)
city = st.text_input("City Name", placeholder="Enter a city name")
if st.button("Get Weather"):
    api_key = "473f48be75d6fc2db51aef72de128b99"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response=requests.get(url)
    if response:
        data=response.json()
        st.write(f"Weather in city: {data['name']},{data['sys']['country']}")
        st.write(f"Temperature: {data['main']['temp']} °C")
        st.write(f"Weather: {data['weather'][0]['description'].title()}")
        st.write(f"Humidity: {data['main']['humidity']} %")
        st.write(f"Wind speed: {data['wind']['speed']} m/s")
        st.success("Weather data fetched successfully!")
    else:
        st.error("City not found or API error. Please try again.")


#https://api.openweathermap.org/data/2.5/weather?q=chennai&appid=76abbf79faa2491a0e071368e9c07996&units=metric