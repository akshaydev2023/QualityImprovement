import pip

# List the required libraries here (replace placeholders with actual names):
required_libraries = [
    "datetime",
    "pyautogui",
    "os",
    "easyocr",
    # ... and so on
]

# Install each library using pip
for library in required_libraries:
    pip.main(['install', library])

print("All required libraries installed successfully!")
