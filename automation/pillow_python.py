from PIL import Image
import os

# Load the images
known_screenshot = Image.open('known_screenshot.png')
current_screenshot = Image.open('dashboard_screenshot.png')

# Compare the images
diff = ImageChops.difference(known_screenshot, current_screenshot)

# Save the difference image
diff.save('diff_screenshot.png')

# Check if the images are identical
if diff.getbbox():
    print("The images are different.")
else:
    print("The images are identical.")

