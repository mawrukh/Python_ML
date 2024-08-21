import streamlit as st
from PIL import Image
import requests
from io import BytesIO

def pixelate_image(image, pixel_size):
    # Resize the image to a smaller size
    small = image.resize(
        (image.width // pixel_size, image.height // pixel_size), 
        resample=Image.NEAREST
    )
    # Scale it back to the original size
    result = small.resize(image.size, Image.NEAREST)
    return result

# Streamlit App
st.title("Pixelate Image Converter")

# Choose between URL or file upload
option = st.radio("Choose image source:", ("Upload Image", "Enter Image URL"))

if option == "Upload Image":
    # Upload an image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open the image file
        image = Image.open(uploaded_file)

elif option == "Enter Image URL":
    # Input URL
    image_url = st.text_input("Enter image URL:", placeholder="https://example.com/image.jpg")

    if image_url:
        try:
            # Download the image from the URL
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
        except Exception as e:
            st.error(f"An error occurred while fetching the image: {str(e)}")
            st.stop()

if 'image' in locals():
    # Pixelate the image with a pixel size of 4 (you can adjust this value)
    pixel_size = 4
    image_pixelated = pixelate_image(image, pixel_size)

    # Create columns for side-by-side display
    col1, col2 = st.columns(2)

    with col1:
        # Display the original image
        st.image(image, caption="Original Image", width=350)

    with col2:
        # Display the pixelated image
        st.image(image_pixelated, caption="Pixelated Image", width=350)
