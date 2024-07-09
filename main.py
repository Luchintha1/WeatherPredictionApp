import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select Number of Days for the Prediction")
mode = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{mode} for the next {days} days in {place}")

if place:
    filtered_data = get_data(place, days)

try:
    # filtering data according to the mode
    if mode == "Temperature":
        temperatures = [dic["main"]["temp"]/10 for dic in filtered_data]
        dates = [dic['dt_txt'] for dic in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", 'y': 'Temperature (C)'})
        st.plotly_chart(figure)
    elif mode == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}

        sky_conditions = [dic['weather'][0]['main'] for dic in filtered_data]
        images_path = [images[conditions] for conditions in sky_conditions]
        st.image(images_path, width=115)
except NameError:
    st.write("Please enter Place.")

except TypeError:
    st.write("Please Enter an Existing Place")


