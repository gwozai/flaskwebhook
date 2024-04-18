import io
import requests
import base64
import hashlib
from PIL import Image
from io import BytesIO

def fetch_and_encode_image(url):
    # Fetch the image from the URL
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful

    # Convert image to a format suitable for base64 encoding
    image = Image.open(BytesIO(response.content))
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    image_data = buffered.getvalue()

    # Encode the image data to base64
    base64_encoded_data = base64.b64encode(image_data).decode('utf-8')

    # Calculate MD5 hash of the original image data
    md5_hash = hashlib.md5(image_data).hexdigest()

    return base64_encoded_data, md5_hash


def encode_image_to_base64(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG")
        image_data = buffered.getvalue()

    # Encode the image data to base64
    base64_encoded_data = base64.b64encode(image_data).decode('utf-8')

    # Calculate MD5 hash of the originaWl image data
    md5_hash = hashlib.md5(image_data).hexdigest()

    return base64_encoded_data, md5_hash


# Example usage:
# base64_data, md5 = encode_image_to_base64('path_to_your_image.jpg')
# print("Base64 Data:", base64_data)
# print("MD5 Hash:", md5)
