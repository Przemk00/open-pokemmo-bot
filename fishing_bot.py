import pyautogui
import time
import sys
import random
import contextlib
from PIL import Image
import pytesseract
import time
import re
import os

#from utils import *
from constants import *
from config import *
from utils import *

def talkToReceptionist():
    print('Talking to receptionist')
    pressKey('up', 2.2)
    pressKey('z', 11, 1.1)
    time.sleep(1.4)

def walkToFishingSpot():
    print('Walk to fishing spot')
    pressKey('up', 2.2)
    pressKey('right', 1.4)
    pressKey('up', .4)

def capture_screen_and_read_balls():
    # Define the path where the screenshot will be saved
    screenshot_path = os.path.join(os.getcwd(), "captured_screenshot.png")

    # Capture a screenshot and save it
    ss = pyautogui.screenshot(screenshot_path)
    ss.save(screenshot_path)
    #print(f"Screenshot captured and saved to {screenshot_path}")

    # Add a delay to ensure the file is written to disk
    time.sleep(1)

    # Check if the file exists before trying to open it
    if not os.path.exists(screenshot_path):
        #print(f"Error: Screenshot file not found at {screenshot_path}")
        return

    # Load the screenshot
    image = Image.open(screenshot_path)

    # Use Tesseract to perform OCR on the image
    text = pytesseract.image_to_string(image)

    sanitized_text = re.sub(r'\s+', ' ', text).strip()

    # Search for the specific part of the text that indicates the number of balls left
    match = re.search(r'Attempt to catch\. \((\d+) left\.\)', sanitized_text, re.IGNORECASE)
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
    
def tryToFish():
    print('Try to catch a fish')
    pressKey(OLD_ROD_KEY)
    time.sleep(5)
    try:
        # Check if fish is hooked or not
        fishIsHooked = pyautogui.locateOnScreen('poke_img/720_landed_a_pokemon_0.png', confidence=0.6)
    except pyautogui.ImageNotFoundException:
        fishIsHooked = None 
    try:
        noFishHooked = pyautogui.locateOnScreen('poke_img/720_not_even_a_nibble_0.png', confidence=0.6)
    except pyautogui.ImageNotFoundException:
        noFishHooked = None
    
     # Check if either image was found
    if fishIsHooked is not None:
        print("Fish is hooked!")
    elif noFishHooked is not None:
        print("No fish hooked.")
    else:
        print("Failed to identify hook status. Neither fish hooked nor no fish hooked detected.")
        return  # Exit the function if neither image was found
        
    if fishIsHooked is not None:
        time.sleep(3)
        pressKey('z')
        result = catchFish()
        if result == 'success':
            time.sleep(2)
            # Dismiss summary screen
            pressKey('esc')
        return result
    else: 
        time.sleep(2)
        pressKey('x')
        return 'failed'

def catchFish():
    while True:
        time.sleep(2)
        pressKey('z')
        time.sleep(3.5)
        # Check for 'fled' result
        with contextlib.suppress(pyautogui.ImageNotFoundException):
            print("Checking for 'fled' result...")
            fledResult = pyautogui.locateOnScreen('poke_img/720_fled_from.png', confidence=0.7)
            #print(f"Fled result: {fledResult}")
            if fledResult is not None:
                print('FLED...')
                pressKey('esc')
                return 'failed'

        # Check for 'summary' result
        with contextlib.suppress(pyautogui.ImageNotFoundException):
            print("Checking for 'summary' result...")
            pokeSummaryShown = pyautogui.locateOnScreen('poke_img/720_pokemon_summary_0.png', confidence=0.6)
            #print(f"Summary result: {pokeSummaryShown}")
            if pokeSummaryShown is not None:
                print('Pokemon caught!')
                time.sleep(2)
                return 'success'

        balls_left = capture_screen_and_read_balls()
        if balls_left is not None:
            if balls_left == 0:
                print("No Pokéballs left, performing key presses.")
                pressKey('down')
                pressKey('right')
                pressKey('z')
                return 'quit'  # Exits the function and returns 'quit'
            else:
                print(f"Balls left: {balls_left}. Continuing with the process...")
            
        print("No result yet, waiting or throwing another ball...")

def main():
    talkToReceptionist()
    walkToFishingSpot()
    time.sleep(3)
    for i in range(30):
            print(f"Attempt {i + 1} of 30:")
            result = tryToFish()
            if result == 'failed':
                print("Attempt failed, moving to the next one.")
            if result == 'quit':
                sys.exit()
            else:
                print("Fish caught successfully!")

if __name__ == "__main__":
    main()


