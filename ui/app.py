import streamlit as st
import requests
from PIL import Image
import numpy as np
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.models import load_model
import io

# # Define the Rust API endpoint URL
# API_URL = "http://localhost:8503/api/chat"  # Adjust the port if needed

# # Load pre-trained models
# model_label = load_model(
#     "./bestmodel.keras",
#     compile=False,
# )

# food_subset = [
#     "tiramisu",
#     "tuna_tartare",
#     "beet_salad",
#     "fish_and_chips",
#     "pancakes",
#     "caesar_salad",
#     "garlic_bread",
#     "carrot_cake",
#     "chocolate_mousse",
#     "hot_dog",
#     "steak",
# ]
# food_subset.sort()


# # Function to predict class name from image
# def predict_class_name(img_data):
#     img = Image.open(io.BytesIO(img_data))
#     img = img.resize((299, 299)).convert("RGB")
#     img_array = np.array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array = preprocess_input(img_array)

#     predictions = model_label.predict(img_array)
#     predicted_class_index = np.argmax(predictions)
#     predicted_class_name = food_subset[predicted_class_index]

#     return predicted_class_name


# # Streamlit app title
# st.title("Dish Classifier and Recipe Assistant")

# # Upload image URL
# image_url = st.sidebar.text_input("Image URL")

# # Define columns for layout
# col1, col2, col3 = st.columns(3)

# # Check if an image URL is provided
# if image_url:
#     try:
#         # Download the image from the URL
#         response = requests.get(image_url)
#         if response.status_code == 200:
#             # Open the image from the response content
#             img_data = response.content
#             predicted_class_name = predict_class_name(img_data)

#             # Display the uploaded image
#             img = Image.open(io.BytesIO(img_data))
#             resized_img = img.resize((250, 200))
#             col1.write("#### Uploaded Image:")
#             col1.image(resized_img, caption="Uploaded Image", use_column_width=True)

#             # Display the predicted label
#             col3.write("#### Predicted Dish:")
#             col3.write(predicted_class_name)
#         else:
#             st.sidebar.error("Error: Failed to download the image.")
#     except Exception as e:
#         st.sidebar.error(f"Error: {e}")
# else:
#     st.sidebar.warning("Please enter an image URL.")

# # Title for user prompt
# st.header("What do you want to know about the dish?")

# # Input prompt from the user
# prompt = st.text_area("Enter your prompt:")
# result_display = st.empty()  # Empty container to display the result

# # Submit button to generate response
# if st.button("Generate Response"):
#     if not prompt:
#         st.warning("Please enter a prompt.")
#     elif "predicted_class_name" not in globals():
#         result_display.error("Please upload an image first.")
#     else:
#         try:
#             with st.spinner("Generating response..."):
#                 # Combine the user's prompt with the predicted dish label
#                 prompt_with_dish = f"{prompt} {predicted_class_name}"
#                 # Make a POST request to the Rust API
#                 response = requests.post(API_URL, json={"prompt": prompt_with_dish})
#                 if response.status_code == 200:
#                     result = response.json().get("response")
#                     result_display.success(f"{result}")
#                 else:
#                     result_display.error("Error: Failed to generate a response.")
#         except requests.exceptions.RequestException as e:
#             result_display.error(f"Error f: {e}")


# # from tensorflow.keras.applications.inception_v3 import preprocess_input
# # from tensorflow.keras.models import load_model
# import io

# Define the Rust API endpoint URL
API_URL = "http://127.0.0.1:8080/query"  # Adjust the port if needed

# Load pre-trained models
model_label = load_model(
    "./bestmodel.keras",
    compile=False,
)

food_subset = [
    "tiramisu",
    "tuna_tartare",
    "beet_salad",
    "fish_and_chips",
    "pancakes",
    "caesar_salad",
    "garlic_bread",
    "carrot_cake",
    "chocolate_mousse",
    "hot_dog",
    "steak",
]

food_subset_dict = {
    "tiramisu": "Tiramisu",
    "tuna_tartare": "Tuna Tartare",
    "beet_salad": "Beet Salad",
    "fish_and_chips": "Fish and Chips",
    "pancakes": "Pancakes",
    "caesar_salad": "Caesar Salad",
    "garlic_bread": "Garlic Bread",
    "carrot_cake": "Carrot Cake",
    "chocolate_mousse": "Chocolate Mousse",
    "hot_dog": "Hot Dog",
    "steak": "Steak",
}
food_subset.sort()


# Function to predict class name from image
def predict_class_name(img_data):
    img = Image.open(io.BytesIO(img_data))
    img = img.resize((299, 299)).convert("RGB")
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model_label.predict(img_array)
    predicted_class_index = np.argmax(predictions)
    predicted_class_name = food_subset[predicted_class_index]

    return predicted_class_name


# Streamlit app title
st.title("Dish Classifier and Recipe Assistant")

# Upload image URL
image_url = st.sidebar.text_input("Image URL")
st.sidebar.markdown(
    "Please enter an image URL of one of the following items:\n- Tiramisu\n- Tuna Tartare\n- Beet Salad\n- Fish and Chips\n- Pancakes\n- Caesar Salad\n- Garlic Bread\n- Carrot Cake\n- Chocolate Mousse\n- Hot Dog\n- Steak",
    unsafe_allow_html=True,
)
# Define columns for layout
col1, col2, col3 = st.columns(3)

# Check if an image URL is provided
if image_url:
    try:
        # Download the image from the URL
        response = requests.get(image_url)
        if response.status_code == 200:
            # Open the image from the response content
            img_data = response.content
            predicted_class_name = predict_class_name(img_data)

            # Display the uploaded image
            img = Image.open(io.BytesIO(img_data))
            resized_img = img.resize((250, 200))
            col1.write("#### Uploaded Image:")
            col1.image(resized_img, caption="Uploaded Image", use_column_width=True)

            # Display the predicted label
            col3.write("#### Predicted Dish:")
            col3.write(food_subset_dict[predicted_class_name])
        else:
            st.sidebar.error("Error: Failed to download the image.")
    except Exception as e:
        st.sidebar.error(f"Error: {e}")
else:
    st.sidebar.warning("Please enter an image URL.")

# Title for user prompt
st.header("What do you want to know about the dish?")

# Input prompt from the user
prompt = st.text_area("Enter your prompt:")
result_display = st.empty()  # Empty container to display the result

# Submit button to generate response
if st.button("Generate Response"):
    if not prompt:
        st.warning("Please enter a prompt.")
    elif "predicted_class_name" not in globals():
        result_display.error("Please upload an image first.")
    else:
        try:
            with st.spinner("Generating response..."):
                # Combine the user's prompt with the predicted dish label
                prompt_with_dish = f"Dish: {food_subset_dict[predicted_class_name]}, Question: {prompt}"
                # Make a POST request to the Rust API
                response = requests.post(API_URL, json={"inputs": prompt_with_dish})
                if response.status_code == 200:
                    result = response.json()  # .get("generated_response")
                    generated_text = result[0]["generated_text"]
                    result_display.success(f"{generated_text}")
                else:
                    result_display.error("Error: Failed to generate a response.")
        except requests.exceptions.RequestException as e:
            result_display.error(f"Error: {e}")
