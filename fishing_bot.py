2# fishing_bot.py
import pyautogui
import time
import sys
import random

from utils import *
from constants import *
from config import *

# Importing functions from your original script (assuming it's named original_bot.py)
from original_bot import (
    talkToReceptionist,
    walkToFishingSpot,
    catchFish,
    simpleFishLoop,
)

def kantoFish():
    print('Begin Kanto safari fish!')
    # start fishing loop
    numFish = 30
    while(numFish > 0):
        num = randomTime()
        if (num < .08):
            checkPokedex()
        elif (num > .95):
            checkTrainer()
        result = tryToFish()
        print('Fish result:', result)
        if (result == 'success'):
            numFish -= 1
        if (result == 'Failed to identify hook'):
            return
    # Finish safari sequence
    time.sleep(1)
    pressKey('esc')
    pressKey('z', 3)

def tryToFish():
    print('Try to catch a fish')
    # Randomize start time
    time.sleep(randomTime())
    pressKey(OLD_ROD_KEY)
    # Wait for fishing timer
    time.sleep(2.2)
    # Check if fish was hooked
    for i in range(4):
        noFishHooked = pyautogui.locateOnScreen('poke_img/720_not_even_a_nibble_' + str(i) + '.png')
        fishIsHooked = pyautogui.locateOnScreen('poke_img/720_landed_a_pokemon_' + str(i) + '.png')
        print('hooked', fishIsHooked, noFishHooked)
        if (noFishHooked != None or fishIsHooked != None):
            break
    hooked = False
    if (fishIsHooked != None):
        hooked = True
    elif (noFishHooked == None):
        return 'Failed to identify hook'
    if (hooked):
        print('Fish is hooked!')
        # Dismiss "Landed a Pokemon" message
        pressKey('z')
        # Wait for battle to start
        time.sleep(5.9)
        result = catchFish()
        if (result == 'success'):
            time.sleep(randomTime())
            # Dismiss summary screen
            pressKey('esc')
            return result
    else:
        pressKey('z')
        return 'failed'

def main():
    # Initialize PyAutoGUI
    pyautogui.FAILSAFE = True
    time.sleep(5)
    # Start fishing process
    print("Starting the fishing process...")
    kantoFish()  # or simpleFishLoop() depending on what you want to run

    print("Fishing done!")

if __name__ == "__main__":
    main()
