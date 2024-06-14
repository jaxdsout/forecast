import streamlit as st
import matplotlib

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5, value=1,
                 help="Select number of days to forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")




