import cv2
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt
import re

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"


def extract_receipt():
    image = cv2.imread('sample.png', cv2.IMREAD_GRAYSCALE)
    extracted_text = pytesseract.image_to_string(image)

    # For final amount
    amounts = re.findall(r'\d+\.\d{2}\b', extracted_text)
    floats = [float(amount) for amount in amounts]
    unique = list(dict.fromkeys(floats))
    return max(unique)
