import cv2
import numpy as np
import pyautogui
import time

def capture_screenshot():
    """Capture a screenshot of the current screen."""
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)  # Convert to numpy array (OpenCV format)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # Convert from RGB to BGR
    return screenshot

def find_template_on_screen(template_paths, threshold=0.6):
    """Find any of the given templates on the screen."""
    # Capture the current screen
    screenshot = capture_screenshot()

    for template_path in template_paths:
        # Load the template image (ore screenshot)
        template = cv2.imread(template_path, cv2.IMREAD_COLOR)

        # Perform template matching
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

        # Get locations of matches with confidence above the threshold
        locations = np.where(result >= threshold)

        # If matches are found, return the first matched location
        if len(locations[0]) > 0:
            # Get the first match (you can modify to handle multiple matches if needed)
            pt = (locations[1][0], locations[0][0])
            print(f"Match found with template: {template_path}")
            return pt  # Return the coordinates of the matched region

    print("No matches found.")
    return None

def click_on_location(location):
    pyautogui.press('z')
    """Click at the specified (x, y) location."""
    x, y = location
    pyautogui.moveTo(x + 50, y + 30, duration=0.5)
    pyautogui.click()  # Offset slightly to click inside the matched region
    print(f"Clicked at: ({x}, {y})")
    # Wait for 5 seconds before searching again
    time.sleep(8)
    pyautogui.press('z')

# List of template images (the ore screenshots)
template_images_paths = [
    'vein1.png',
    'vein2.png',
    'vein3.png',
    'vein4.png',
    'vein5.png',
    'vein6.png',
    'vein7.png',
    'vein8.png',
    'vein9.png',
    'vein10.png',
    'vein11.png'
]

# Main loop
while True:
    # Find any of the ores on the screen
    ore_location = find_template_on_screen(template_images_paths, threshold=0.6)

    if ore_location:
        # Click the ore if found
        click_on_location(ore_location)



