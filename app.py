import os
import textwrap

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Google Generative AI API
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key not found. Please set the GOOGLE_API_KEY environment variable.")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    # Function to get responses from the Gemini model
    def get_gemini_response(question):
        response = model.generate_content(question)
        return response.text

    # Initialize the Streamlit app
    st.set_page_config(page_title="Q&A Demo")
    st.header("Gemini Application")

    # User input
    user_input = st.text_input("Input: ", key="input")
    submit = st.button("Ask the question")

    # If ask button is clicked
    if submit:
        if user_input:
            response = get_gemini_response(user_input)
            st.subheader("The Response is")
            st.markdown(response)  # Use Streamlit's markdown rendering
        else:
            st.error("Please enter a question.")

