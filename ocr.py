import cv2
import easyocr
import re

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

def extract_receipt():
    # Read the image using OpenCV
    image = cv2.imread('static/sample.png')  # Ensure the path is correct
    # Convert image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Use EasyOCR to extract text
    results = reader.readtext(image_rgb)

    # Combine the extracted text into a single string
    extracted_text = ' '.join([result[1] for result in results])

    # Extract monetary amounts from the extracted text
    amounts = re.findall(r'\d+\.\d{2}\b', extracted_text)
    floats = [float(amount) for amount in amounts]
    unique = list(dict.fromkeys(floats))
    
    # Return the maximum unique amount
    return max(unique) if unique else None
