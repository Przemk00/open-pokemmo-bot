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
import logging

from utils import *
from constants import *
from config import *

def talkToReceptionist():
    logger.info('Talking to receptionist...')
    pressKey('z', 11, 1.1)
    time.sleep(1.4)

def walkToFishingSpot():
    logger.info('Walk to fishing spot...')
    holdKey('up', 1.5)
    holdKey('right', 0.95)
    holdKey('up', .4)

def catchFish():
    while True:
        time.sleep(0.5)
        with contextlib.suppress(pyautogui.ImageNotFoundException):
            #logger.info("Checking for 'fled' result...")
            fledResult = pyautogui.locateOnScreen('poke_img/720_fled_from.png', confidence=0.7)
            #logger.info(f"Fled result: {fledResult}")
            if fledResult is not None:
                logger.warning('FLED...')
                return 'failed'

        with contextlib.suppress(pyautogui.ImageNotFoundException):
            #logger.info("Checking for 'summary'...")
            pokeSummaryShown = pyautogui.locateOnScreen('poke_img/720_pokemon_summary_0.png', confidence=0.6)
            #logger.info(f"Summary result: {pokeSummaryShown}")
            if pokeSummaryShown is not None:
                logger.info('Pokemon caught!')
                time.sleep(2)
                return 'success'
            
        #logger.info("No result yet...")

def tryToFish():
    logger.info('Try to catch a fish...')
    pressKey(OLD_ROD_KEY)
    time.sleep(4.5)
    try:
        fishIsHooked = pyautogui.locateOnScreen('poke_img/720_landed_a_pokemon_0.png', confidence=0.6)
    except pyautogui.ImageNotFoundException:
        fishIsHooked = None 
    try:
        noFishHooked = pyautogui.locateOnScreen('poke_img/720_not_even_a_nibble_0.png', confidence=0.6)
    except pyautogui.ImageNotFoundException:
        noFishHooked = None
    
    if fishIsHooked is not None:
        logger.info("Fish is hooked...")
    elif noFishHooked is not None:
        logger.info("No fish hooked...")
    else:
        logger.info("Failed to identify hook status. Neither fish hooked nor no fish hooked detected...")
        return 
        
    if fishIsHooked is not None:
        time.sleep(3.0)
        pressKey('z')
        time.sleep(5.0)
        pressKey('down')
        time.sleep(0.5)
        pressKey('z')
        time.sleep(1.5)
        with contextlib.suppress(pyautogui.ImageNotFoundException):
                logger.info("Check if Pokémon fled...")
                fledResult = pyautogui.locateOnScreen('poke_img/720_fled_from.png', confidence=0.6)
                if fledResult is not None:
                    logger.info('FLED...')
        #            pressKey('esc')
                    return 'failed'        
        
        time.sleep(4.5)
        pressKey('z')
        time.sleep(0.5)
        result = catchFish()
        if result == 'success':
            time.sleep(2)
            pressKey('esc')
        return result
    else: 
        time.sleep(2)
        pressKey('x')
        return 'failed'

# def simpleFishLoop():
#     numFish = 0
#     if (len(sys.argv) >= 3):
#         numFish = int(sys.argv[2])
#     else:
#         numFish = 1
#     while(numFish > 0):
#         result = tryToFish()
#         if (result == 'success'):
#             numFish -= 1
#         if (result == 'Failed to identify hook...'):
#             return

def kantoFish():
    logger.info('Begin Kanto safari fish...')
    
    while True:
        # Initial steps before starting the fishing loop
        holdKey('up', .4)
        talkToReceptionist()
        walkToFishingSpot()
        
        numFish = 30
        while numFish > 0:
            result = tryToFish()
            if result == 'Failed to identify hook...':
                return
            elif result == 'success':
                numFish -= 1
                logger.info(f'Number of Pkmn left to catch: {numFish}')
        
        # If numFish reaches 0, press 'z' 5 times, and restart kantoFish
        logger.info('No more fish left. Pressing "z" 6 times and restarting fishing...')
        time.sleep(10)
        pressKey('z', 6)
        time.sleep(3)    
        # Repeat the initial steps before restarting the fishing loop
        logger.info('Restarting Kanto safari fish...')


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
    
def main():
    # Initialize PyAutoGUI
    pyautogui.FAILSAFE = True
    time.sleep(3)
    kantoFish()
    logger.info("Done")
if __name__ == "__main__":
    main()  

