import pyautogui
import time

def testPokemonSummaryDetection():
    time.sleep(3)  # Give yourself time to bring the correct screen in focus

    # Capture the screen for debugging purposes
    pyautogui.screenshot('debug_screenshot.png')

    # Attempt to locate the summary image
    try:
        pokeSummaryShown = pyautogui.locateOnScreen('poke_img/720_pokemon_summary_0.png', confidence=0.6)
        if pokeSummaryShown is not None:
            print(f"Pokemon Summary Found at: {pokeSummaryShown}")
        else:
            print("Pokemon Summary not found.")
    except pyautogui.ImageNotFoundException:
        print("ImageNotFoundException: Could not locate the summary image.")

def main():
    testPokemonSummaryDetection()

if __name__ == "__main__":
    main()
