import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
location = st.text_input("Location")
days = st.slider("Forecast Days", min_value=1, max_value=5, value=1,
                 help="Select number of days to forecast")
field = st.selectbox("Select data to view", ("Temperature", "Sky"))

if location:
    try:
        filtered_data = get_data(location, days)
        if field == "Temperature":
            st.subheader(f"{field} for the next {days} days in {location}")
            temps = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(
                x=dates,
                y=temps,
                labels={
                    "x": "Date",
                    "y": "Temperature (c)"
                }
            )
            st.plotly_chart(figure)

        if field == "Sky":
            st.subheader(f"{field} for the next {days} days in {location}")
            images = {
                "Clear": "images/clear.png",
                "Snow": "images/snow.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
            }
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.text("Not a valid city. Or not currently in our directory. Please try again")

