import pyautogui
from PIL import Image
import pytesseract
import time
import re
import os

def capture_screen_and_read_balls():
    # Define the path where the screenshot will be saved
    screenshot_path = os.path.join(os.getcwd(), "captured_screenshot.png")

    # Capture a screenshot and save it
    pyautogui.screenshot(screenshot_path)
    print(f"Screenshot captured and saved to {screenshot_path}")

    # Check if the file exists before trying to open it
    if not os.path.exists(screenshot_path):
        print(f"Error: Screenshot file not found at {screenshot_path}")
        return

    # Load the screenshot
    image = Image.open(screenshot_path)

    # Use Tesseract to perform OCR on the image
    text = pytesseract.image_to_string(image)

    # Print the extracted text for debugging
    print("Extracted Text:")
    print(text)

    # Search for the specific part of the text that indicates the number of balls left
    match = re.search(r'Attempt to catch\. \((\d+) left\.\)', text)
    if match:
        balls_left = match.group(1)
        print(f"Balls left: {balls_left}")
    else:
        print("Could not find the number of balls left.")

def main():
    time.sleep(3)  # Give yourself time to focus the window you want to capture
    capture_screen_and_read_balls()

if __name__ == "__main__":
    main()
