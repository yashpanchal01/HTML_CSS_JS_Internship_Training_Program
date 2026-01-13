import streamlit as st
import google.generativeai as genai

st.title("Gemini webapp!")
user_input = st.text_input("ask me anything!")

genai.configure(api_key="AIzaSyA7RkdiYX0K6h_C8MAYXZm4ao-p92QG1eM")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if user_input:
    with st.spinner("Thinking..."):
        response = model.generate_content(user_input)
        st.write(response.text)




