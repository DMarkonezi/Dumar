import pyautogui
import time
import pyperclip

def getUrl():
    # Focus on Chrome (assuming it's open)
    pyautogui.hotkey('alt', 'tab')  # Switch to Chrome
    time.sleep(1)

    # Select the address bar (shortcut: Ctrl+L or F6)
    pyautogui.hotkey('ctrl', 'l')  # Or 'f6'
    time.sleep(0.5)

    # Copy the URL (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    # Get the URL from clipboard
    url = pyperclip.paste()
    print("Current URL:", url)

