import pyautogui
import datetime

def take_screenshot(filename="screenshot.png", save_path="."):
    """Takes a screenshot of the entire screen and saves it as a PNG image.

    Args:
        filename (str, optional): The name of the screenshot file. Defaults to "screenshot.png".
        save_path (str, optional): The path where the screenshot should be saved. Defaults to the current directory.
    """

    try:
        # Capture the screenshot
        image = pyautogui.screenshot()

        # Generate a unique filename with timestamp if not provided
        if filename == "screenshot.png":
            filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

        # Construct the full save path
        full_path = f"{save_path}/{filename}"

        # Save the screenshot to the specified path
        image.save(full_path)

        print(f"Screenshot saved successfully to: {full_path}")
    except Exception as e:
        print(f"Error saving screenshot: {e}")

# Example usage:
take_screenshot(filename="my_custom_screenshot.png", save_path="C:/Users/BIPL-GEN-03/Desktop/QVF Project/Screenshots")
