import pip
import tkinter as tk  # Import tkinter for popup message

# Replace placeholders with the actual library names:
required_libraries = [
    "library_name1",
    "library_name2",
    "library_name3",
    # ... and so on
]

for library in required_libraries:
    try:
        pip.main(['install', library])
    except Exception as e:
        # Create a popup window to display the error message
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        tk.messagebox.showerror("Installation Error", f"An error occurred while installing {library}: {e}")
        break  # Stop installation if an error occurs

if not any(error for error in required_libraries):
    print("All required libraries installed successfully!")
