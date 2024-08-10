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

from utils import *
from constants import *
from config import *

def checkPokedex():
    time.sleep(.2)
    pressKey('n')
    time.sleep(0.2 + randomTime() * 3)
    pressKey('n')

def checkTrainer():
    time.sleep(.2)
    pressKey('c')
    time.sleep(0.2 + randomTime() * 3)
    pressKey('c')

def talkToReceptionist():
    print('Talking to receptionist')
    pressKey('z', 11, 1.1)
    time.sleep(1.4)

def walkToFishingSpot():
    print('Walk to fishing spot')
    holdKey('up', 1.5)
    holdKey('right', 0.9)
    holdKey('up', .4)
 #   holdKey('left', .4)

def catchFish():
    while True:
        time.sleep(2)
        # Check for 'fled' resultz
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
            
        print("No result yet, waiting or throwing another ball...")

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
        time.sleep(4.5)
        pressKey('z')
        time.sleep(5.5)
        pressKey('down')
        time.sleep(0.5)
        pressKey('z')
        time.sleep(4.5)
        pressKey('z')
        time.sleep(0.5)
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

def simpleFishLoop():
    # Check if the user specified how many
    # fish to catch
    numFish = 0
    if (len(sys.argv) >= 3):
        numFish = int(sys.argv[2])
    else:
        numFish = 1
    while(numFish > 0):
        result = tryToFish()
        print('Fish result:', result)
        if (result == 'success'):
            numFish -= 1
        if (result == 'Failed to identify hook'):
            return

def kantoFish():
    print('Begin Kanto safari fish!')
    #holdKey('up', .4)
    #talkToReceptionist()
    walkToFishingSpot()
    numFish = 30
    while (numFish > 0):
        result = tryToFish()
        print('Fish result:', result)
        if result == 'Failed to identify hook':
            return
        elif result == 'success':
            numFish -= 1
    # Finish safari sequence
    time.sleep(1)
    pressKey('esc')
    pressKey('z', 3)

def walkToIsland2Grass():
    # Mount bike
    pressKey('4')
    # Ride to spot
    holdKey('right', .55)
    holdKey('up', .35)
    holdKey('right', .7)
    holdKey('up', 1)
    holdKey('left', .7)
    holdKey('up', 1)

def island2Payday():
    walkToIsland2Grass()

def walkToIsland5Grass():
    # Mount bike
    pressKey('4')
    # Ride to spot

def island5Payday():
    walkToIsland5Grass()

def main():
    # Initialize PyAutoGUI
    pyautogui.FAILSAFE = True

    if (len(sys.argv) == 1):
        print("Loading default fisher")
        startCountDown()
        kantoFish()
    elif (sys.argv[1] == "fish"):
        print("Fishing...")
        startCountDown()
        simpleFishLoop()
    elif (sys.argv[1] == "payday"):
        print("Payday time...")
        startCountDown()
        island2Payday()

    print("Done")

if __name__ == "__main__":
    main()  
2