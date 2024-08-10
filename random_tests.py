import pyautogui
import time

def pressKey(key):
    pyautogui.press(key)

def catchFish():
    while True:
        time.sleep(2)
        pressKey('z')
        time.sleep(5)

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
    time.sleep(3)  # Give time to switch to the correct window
    result = catchFish()
    print(f"Catch Fish Result: {result}")

if __name__ == "__main__":
    main()
