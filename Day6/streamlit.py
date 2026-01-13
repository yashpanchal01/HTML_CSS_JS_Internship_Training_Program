import streamlit as st



st.title("My streamlit app")
name = st.text_input('ennter your name!')

if st.button('submit'):
    st.write('hello', name)

age = st.slider("Enter your age", 1, 100)
city = st.selectbox("choose your city", ["delhi", "mumbai", "Chenai", "kolkata"])


if st.button ("show details"):
    st.write("age", age)
    st.write("City:" city)
    