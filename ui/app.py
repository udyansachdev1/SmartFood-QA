import streamlit as st
import requests
from PIL import Image
import numpy as np
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.models import load_model


# Define function to load and preprocess image
def load_and_preprocess_image(image_file, target_size):
    img = Image.open(image_file)
    img = img.resize(target_size).convert("RGB")
    img = np.array(img)
    return img


def predict_class(model, image):
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
    food_subset.sort()

    img_array = np.expand_dims(image, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions)
    predicted_class = food_subset[predicted_class_index]
    return predicted_class


# Define the Rust API endpoint URL
API_URL = "http://localhost:8503/api/chat"  # Adjust the port if needed

# Streamlit app title
st.title("Dish Classifier and Recipe Assistant")

# Upload image
uploaded_file = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Define columns for layout
col1, col2, col3 = st.columns(3)

# Check if an image is uploaded
if uploaded_file is not None:
    # Display the uploaded image
    img = Image.open(uploaded_file)
    resized_img = img.resize((250, 200))
    col1.write("#### Uploaded Image:")
    col1.image(resized_img, caption="Uploaded Image", use_column_width=True)

    # Load pre-trained models
    model_label = load_model(
        "../bestmodel.keras",
        compile=False,
    )
    processed_image = load_and_preprocess_image(uploaded_file, (299, 299))

    # Predict class name
    predicted_class_name = predict_class(model_label, processed_image)

    # Display the predicted label
    col3.write("#### Predicted Dish:")
    col3.write(predicted_class_name)
else:
    st.sidebar.warning("Please upload an image.")

# Title for user prompt
st.header("What do you want to know about the dish?")

# Input prompt from the user
prompt = st.text_area("Enter your prompt:")
result_display = st.empty()  # Empty container to display the result


# Function to generate a response
def generate_response(prompt):
    try:
        if "predicted_class_name" not in globals():
            result_display.error("Please upload an image first.")
            return

        with st.spinner("Generating response..."):
            # Combine the user's prompt with the predicted dish label
            prompt_with_dish = f"{prompt} {predicted_class_name}"
            # Make a POST request to the Rust API
            response = requests.post(API_URL, json={"prompt": prompt_with_dish})
            if response.status_code == 200:
                # print("Response received successfully.")
                result = response.json().get("response")
                # result = "Response received successfully."
                result_display.success(f"{result}")
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
