import streamlit as st
import os
from google import genai
from google.genai import types

# 1. Setup Page Config
st.set_page_config(page_title="Nano Banana Generator", page_icon="🍌")
st.title("Nano Banana Image Generator")

# 2. Secure API Key handling
# Use Streamlit Secrets in production, or an environment variable locally
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    client = genai.Client(api_key="AIzaSyA7RkdiYX0K6h_C8MAYXZm4ao-p92QG1eM")
    
    # User input
    prompt = st.text_input("Enter a detailed image prompt:", 
                          "A photo of a futuristic cat wearing a spacesuit, 4k, cinematic lighting")

    if st.button("Generate Image"):
        if not prompt:
            st.warning("Please enter a prompt.")
        else:
            try:
                st.info("Generating image... this might take a minute.")
                
                # 3. Model call
                # Note: 'imagen-3.0-generate-001' is the standard high-quality model ID
                result = client.models.generate_images(
                    model='imagen-3.0-generate-001', 
                    prompt=prompt,
                    config=types.GenerateImagesConfig(
                        number_of_images=1,
                        output_mime_type="image/png",
                    )
                )

                # 4. Display Logic
                if result.generated_images:
                    # Accessing the bytes from the first generated image
                    generated_image = result.generated_images[0]
                    st.image(generated_image.image.image_bytes, caption=f"Prompt: {prompt}")
                    
                    # Optional: Add a download button
                    st.download_button(
                        label="Download Image",
                        data=generated_image.image.image_bytes,
                        file_name="generated_image.png",
                        mime="image/png"
                    )
                else:
                    st.error("Image generation failed or returned no images.")

            except Exception as e:
                st.error(f"An error occurred: {e}")
else:
    st.info("Please enter your Gemini API Key in the sidebar to get started.")