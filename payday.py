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
        holdKey(RIGHT, 1.7 - randomTime())
        holdKey(LEFT, 1.2 + randomTime())
        holdKey(RIGHT, .7)
        holdKey(LEFT, .3 + randomTime())
        holdKey(RIGHT, 1)
        holdKey(LEFT, .7)
        time.sleep(9)
        result = checkIfWeAreInBattle()
        inBattle = result[0]


def getNewEncounterVertical():
    for i in range(4):
        modifier = random.randrange(0, 1) + 1
        holdKey(DOWN, (.8 + randomTime()) * modifier)
        holdKey(UP, (.7 + randomTime()) * modifier)


def cinnabarPayday():
    bootGame()
    flyBack()
    time.sleep(2)
    while(True):
        isLeftSide = random.randrange(1, 10) > 3
        usePokeCenter()
        if (isLeftSide):
            walkToWaterLeft()
        else:
            walkToWater()
        payDayPP = 20
        while(payDayPP > 6):
            print(payDayPP, "PP left")
            if (isLeftSide):
                getNewEncounterVertical()
            else:
                getNewEncounter()
            payDayPP = resolveBattle(payDayPP)
        print('Fly back to PC')
        print(functionalIndexes)
        flyBack()
        time.sleep(2)


def resolveBattle(payDayPP):
    localPayDayPP = payDayPP
    print('Resolve battle')
    inBattle = True
    detectionCount = 0
    while(inBattle):
        if detectionCount > 1:
            # Exit early if it's a hoard
            pressKey(DOWN)
            pressKey(RIGHT)
            pressKey(A_BUTTON)
        pressKey(UP)
        pressKey(LEFT)
        pressKey(A_BUTTON, 3, .3)
        localPayDayPP -= 1
        time.sleep(14)
        # Check if battle is still going
        result = checkIfWeAreInBattle()
        inBattle = result[0]
        if inBattle:
            if result[1] == 3:
                detectionCount += 1
    return localPayDayPP


def checkIfWeAreInBattle():
    for i in range(5):
        areInBattle = pyautogui.locateOnScreen('poke_img/health_bar_' + str(i) + '.png')
        if (areInBattle != None):
            functionalIndexes.append(i)
            print('Battle detected. Index:', i)
            return [True, i]
    print('No battle detected')
    return [False]


def flyBack():
    pressKey(FLY)
    time.sleep(1)
    pressKey(A_BUTTON)
    time.sleep(3.3 + randomTime())


def walkToWater():
    if (random.randint(1, 2) == 1):
        holdKey(LEFT, .5 + randomTime())
    holdKey(DOWN, .7)
    pressKey(A_BUTTON, 5, .3)
    time.sleep(1.2 + randomTime())


def walkToWaterLeft():
    holdKey(LEFT, 1.4)
    holdKey(UP, .1)
    holdKey(LEFT, .8)
    pressKey(A_BUTTON, 5, .3)
    time.sleep(1.2 + randomTime())


