import streamlit as st
from rembg import remove
from PIL import Image
import base64
from io import BytesIO

# Function to fix the image using rembg
def fix_image(upload):
    image = Image.open(upload)
    fixed = remove(image)
    return fixed

# Function to convert image to base64
def convert_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str

# Function to generate a download link for the image
def get_image_download_link(img):
    """Generates a download link for the given image."""
    img_str = convert_to_base64(img)
    href = f'<a href="data:file/png;base64,{img_str}" download="converted_image.png">Click here to download the image</a>'
    return href

# Add heading and description
st.title("Erase Master")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Check if an image is uploaded
if uploaded_file:
    # Fix the uploaded image
    fixed_image = fix_image(uploaded_file)
    
    # Display the fixed image
    st.image(fixed_image, use_column_width=True)
    
    # Generate and display the download link
    download_link = get_image_download_link(fixed_image)
    st.markdown(download_link, unsafe_allow_html=True)
