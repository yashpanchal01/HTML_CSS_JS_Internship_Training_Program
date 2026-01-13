import google.generativeai as genai 

genai.configure(api_key="AIzaSyA7RkdiYX0K6h_C8MAYXZm4ao-p92QG1eM")

for m in genai.list_models():
    print(m)
