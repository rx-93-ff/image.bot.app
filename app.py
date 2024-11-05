from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
 
load_dotenv()
 
genai.configure(api_key="AIzaSyB5Hu-Mv2VceYQVTZR32BJW6YTQ_P5y4is")
 
st.set_page_config(page_title="Image Chat Bot",page_icon="🗣️")
 
st.header("My Image Chat Bot Web Application of SON")
 
question = st.text_input("Write your question here...")
 
uploaded_image = st.file_uploader("Choose an Image..",type=["jpg","png","jpeg"])
 
image = ""
 
submit = st.button("Submit")
 
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image,caption="Uploaded Image",use_column_width=True)
 
if submit:
    model = genai.GenerativeModel("gemini-1.5-flash")
    if(input!=""):
        response = model.generate_content([question,image])
    else:
        response = model.generate_content(image)
 
    st.write(response.text)