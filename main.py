import shutil  # Used for moving and copying files
from pathlib import Path  # Preferred over os.path for modern and readable path handling

# Define the Downloads folder path dynamically
downloads_path = Path.home() / "Downloads"  # Path.home() gives C:/Users/...
# To verify the path, you can uncomment this:
# print(downloads_path)

# Define file categories and their associated extensions in a dictionary
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".m4a", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

# Freeze the list of files first to avoid issues caused by moving files during iteration
for item in list(downloads_path.iterdir()):  # Iterate through all items (files/folders) in Downloads
    if not item.exists():
        continue  # Skip if the file disappeared (e.g., OneDrive sync)
    
    if item.is_file():  # Proceed only if it’s a file (not a folder)
        moved = False  # Flag to track if the file was sorted into a category

        # Check which category the file belongs to by its extension
        for category, extensions in file_types.items():
            if item.suffix.lower() in extensions:  # .suffix gives extension; .lower() ensures case-insensitive match
                target_folder = downloads_path / category  # Construct the target folder path
                target_folder.mkdir(exist_ok=True)  # Create the folder if it doesn't exist

                # Move the file to the target category folder
                shutil.move(str(item), str(target_folder / item.name))
                # shutil.move requires string paths, so we convert Path objects to strings
                # item.name returns just the filename (e.g., "photo.jpg") — not full path

                print(f"Moved {item.name} to {category}")
                moved = True
                break  # No need to check other categories once matched

        # If file didn't match any category, move it to "Others"
        if not moved:
            other_folder = downloads_path / "Others"
            other_folder.mkdir(exist_ok=True)

            # Double-check file still exists before moving
            if item.exists():
                shutil.move(str(item), str(other_folder / item.name))
                print(f"Moved {item.name} to Others")
