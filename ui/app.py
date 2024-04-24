import streamlit as st
import requests

# Define the Rust API endpoint URL
API_URL = "http://localhost:8502/api/chat"  # Adjust the port if needed

# Streamlit app title
st.title("LLM Inference API in Rust")

# Input prompt from the user
prompt = st.text_area("Enter your prompt:")
result_display = st.empty()  # Empty container to display the result


# Function to generate a response
def generate_response(prompt):
    try:
        with st.spinner("Generating response..."):
            # Make a POST request to the Rust API
            response = requests.post(API_URL, json={"prompt": prompt})
            if response.status_code == 200:
                result = response.json().get("response")
                result_display.success(f"Response: {result}")
            else:
                result_display.error("Error: Failed to generate a response.")
    except requests.exceptions.RequestException as e:
        result_display.error(f"Error: {e}")


# Submit button to generate response
if st.button("Generate Response"):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        generate_response(prompt)
