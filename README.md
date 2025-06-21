# Python File Sorter

A Python automation script that organizes files in your **Downloads** folder by type — Images, Documents, Videos, Audio, Archives, and Others.  
Built to clean up clutter with a single run — beginner-friendly and built only with Python's standard libraries.

---

## Features

- Automatically sorts files into categorized folders
- Uses only built-in Python libraries (`pathlib`, `shutil`)
- Safe for OneDrive-synced folders (handles disappearing files)
- Dynamically creates missing folders
- Easily customizable to add your own categories

---

## How It Works

1. Scans your `Downloads` folder.
2. Categorizes each file based on its extension.
3. Moves the file into a corresponding subfolder.
4. If the extension is not recognized, moves it to the `"Others"` folder.

---

## Tech Used

- Python 3.6+
- `pathlib` — for safe and readable path handling
- `shutil` — for moving files

---

## File Type Categories

| Category   | Extensions                                    |
|------------|-----------------------------------------------|
| Images     | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg` |
| Documents  | `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`, `.csv` |
| Videos     | `.mp4`, `.mov`, `.avi`, `.mkv`               |
| Audio      | `.mp3`, `.wav`, `.m4a`, `.flac`              |
| Archives   | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`         |
| Others     | (Any file not matching the above types)      |



## Setup & Usage

### Requirements

- Python 3.6 or higher
- No external libraries needed

Author
**Aman Malhotra**  

- [GitHub: amanmalhotrainit](https://github.com/amanmalhotrainit)  
- [LinkedIn: amanmalhotrainit](https://www.linkedin.com/in/amanmalhotrainit)
