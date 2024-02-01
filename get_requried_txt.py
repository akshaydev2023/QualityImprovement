import easyocr

reader = easyocr.Reader(['en'])  # Specify languages for detection, e.g., ['en', 'hi'] for English and Hindi

def extract_text_with_easyocr(image_path):
    """Extracts text from an image using EasyOCR.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The extracted text, or an empty string if text extraction fails.
    """

    try:
        result = reader.readtext(image_path, detail=0)  # Set detail=0 to get only text without bounding boxes
        text = '\n'.join(result)  # Join text lines
        return text
    except Exception as e:
        print(f"Error extracting text with EasyOCR: {e}")
        return ""

# Example usage:
image_path = "path/to/your/image.jpg"  # Replace with your image path
extracted_text = extract_text_with_easyocr(image_path)
print(extracted_text)
