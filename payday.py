import pyautogui
import time
import random

from utils import *
from config import *
from common import *


functionalIndexes = []


def getNewEncounter():
    print('Get new encounter')
    inBattle = False
    while(not inBattle):
        holdKey(LEFT, 1)
        holdKey(RIGHT, 1.7)
        holdKey(LEFT, 1.1)
        holdKey(RIGHT, .7)
        holdKey(LEFT, .3)
        holdKey(RIGHT, 1)
        holdKey(LEFT, .7)
        time.sleep(9)
        inBattle = checkIfWeAreInBattle()


def getNewEncounterDumb():
    print('Get new encounter (dumb)')
    holdKey(LEFT, 1.1)
    holdKey(RIGHT, 1.1)
    holdKey(LEFT, 1.7)
    holdKey(RIGHT, 1.7)
    holdKey(LEFT, 1.5)
    holdKey(RIGHT, 1.5)
    holdKey(LEFT, .7)
    time.sleep(7)


def cinnabarPayday():
    while(True):
        usePokeCenter()
        walkToWater()
        payDayPP = 20
        while(payDayPP > 5):
            print(payDayPP, "PP left")
            getNewEncounter()
            payDayPP = resolveBattle(payDayPP)
        print('Fly back to PC')
        print(functionalIndexes)
        flyBack()


def resolveBattle(payDayPP):
    localPayDayPP = payDayPP
    print('Resolve battle')
    inBattle = True
    while(inBattle):
        pressKey(UP)
        pressKey(LEFT)
        pressKey(A_BUTTON, 3, .3)
        localPayDayPP -= 1
        time.sleep(14)
        # Check if battle is still going
        inBattle = checkIfWeAreInBattle()
    return localPayDayPP


def resolveBattleDumb(payDayPP):
    print('Resolve battle')
    pressKey(UP)
    pressKey(LEFT)
    pressKey(UP)
    pressKey(LEFT)
    pressKey(A_BUTTON, 3, .3)
    time.sleep(10)
    return payDayPP - 1


def checkIfWeAreInBattle():
    for i in range(5):
        areInBattle = pyautogui.locateOnScreen('poke_img/health_bar_' + str(i) + '.png')
        if (areInBattle != None):
            functionalIndexes.append(i)
            print('Battle detected. Index:', i)
            return True
    print('No battle detected')
    return False


def flyBack():
    pressKey(FLY)
    time.sleep(1)
    pressKey(A_BUTTON)
    time.sleep(3)


def walkToWater():
    if (random.randint(1, 2) == 1):
        pressKey(LEFT, 3)
    holdKey(DOWN, .7)
    pressKey(A_BUTTON, 5, .3)
    if (random.randint(1, 2) == 1):
        holdKey(DOWN, .3)

