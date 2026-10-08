import streamlit as st
st.title("my first streamlit app")
st.write("hello streamlit!")
name=st.text_input("enter your last name")
if name:
    st.success(f"hello, {name}!")
st.title("My Boss Welcome")
st.header("Header")
st.subheader("Subheader")
st.write("General text")
st.markdown("**Bold** *Italic*")
st.code("print('Hello')")
name = st.text_input("Name")
age = st.number_input("Age", 0, 120)
agree = st.checkbox("I agree")

gender = st.radio("Gender", ["Male", "Female", "Other"])

color = st.selectbox(
    "Favorite color",
    ["Red", "Blue", "Green"]
)

hobbies = st.multiselect(
    "Hobbies",
    ["Sports", "Reading", "Coding"]
)

uploaded_file = st.file_uploader("Upload a file")
if st.button("Click Me"):
    st.write("Button clicked!")
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Age": [24, 30]
})

st.dataframe(df)
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)
st.sidebar.title("Settings")

number = st.sidebar.slider("Choose a number", 0, 100, 50)

st.write("Selected:", number)
col1, col2 = st.columns(2)

with col1:
    st.button("Left")

with col2:
    st.button("Right")

tab1, tab2 = st.tabs(["Home", "About"])

with tab1:
    st.write("Welcome!")

with tab2:
    st.write("About this app")
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(st.session_state.count)
import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Weight (kg)", 30.0, 200.0)
height = st.number_input("Height (m)", 1.0, 2.5)

if st.button("Calculate"):
    bmi = weight / (height ** 2)
    st.success(f"Your BMI is {bmi:.2f}")




