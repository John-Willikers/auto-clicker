import os
import pyautogui
import time
from pyscreeze import ImageGrab

print(os.getcwd())

pyautogui.FAILSAFE = False

# Image file paths
launcher_download_path = "download_launcher.PNG"
website_download_path = "download_website.PNG"
threshold = 0.9

while True:
    try:
        print("Checking for Launcher Download Button")
        screenshot = ImageGrab.grab(all_screens=True)
        launcher_location = pyautogui.locate(launcher_download_path, screenshot, confidence=threshold)

        if launcher_location is not None:
            pyautogui.click(launcher_location.left + 5, launcher_location.top + 5)

        time.sleep(3)

    except Exception as e:
        print(f"Error: {e}. Waiting for the element to appear.")
        time.sleep(3)

    try:
        print("Checking for Website Download Button")
        screenshot = ImageGrab.grab(all_screens=True)
        website_location = pyautogui.locate(website_download_path, screenshot, confidence=threshold)

        if website_location is not None:
            pyautogui.click(website_location.left + 5, website_location.top + 5)

        time.sleep(3)
        print("Waiting for 5 seconds...")
    except Exception as e:
        print(f"Error: {e}. Waiting for the element to appear.")
        time.sleep(3)