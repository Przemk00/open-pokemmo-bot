import pyautogui
import time
import sys
import random

from utils import *
from constants import *
from config import *

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
        return 'failed'

def catchFish():
    while True:
        time.sleep(2)
        pressKey('z')
        time.sleep(3)

        # Check for "fled" image
        try:
            fledResult = pyautogui.locateOnScreen('poke_img/720_fled_from.png', confidence=0.6)
            if fledResult is not None:
                print('FLED:', fledResult)
                return 'failed'
        except pyautogui.ImageNotFoundException:
            pass

        # Check for "summary" image
        try:
            pokeSummaryShown = pyautogui.locateOnScreen('poke_img/720_pokemon_summary_0.png', confidence=0.6)
            if pokeSummaryShown is not None:
                print(f'Pokemon Summary Found at: {pokeSummaryShown}')
                return 'success'
            else:
                print('Summary not found, continuing...')
        except pyautogui.ImageNotFoundException:
            print('Summary ImageNotFoundException, continuing...')

        # If neither "fled" nor "summary" images are found, repeat the loop
        print("No result yet, continuing to wait...")
        time.sleep(0.5)

def main():
    time.sleep(3)
    tryToFish()

if __name__ == "__main__":
    main()
