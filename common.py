import time

from config import *
from utils import *


def usePokeCenter():
    holdKey(UP, 2.5 + randomTime())
    pressKey(A_BUTTON, 7, .6 + randomTime())
    holdKey(DOWN, 1.94)

def bootGame():
    pressKey('win')
    typeWord('pokemmo')
    pressKey('enter')
    time.sleep(10)
    pressKey(A_BUTTON, 3, 3)