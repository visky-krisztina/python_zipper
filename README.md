# 📦 Files Zipper

This is a very simple Python GUI application that allows users to **select multiple files** and **compress them into a ZIP archive** at a specified destination folder.

## 🧰 Modules Used

* FreeSimpleGUI - Python Simple GUI software - Used for creating the graphical user interface: https://pypi.org/project/FreeSimpleGUI/
* **zipfile**: Python's built-in module to create and manage ZIP archives.
* **pathlib**: Provides object-oriented filesystem paths.


## 🗂️ How It Works

1. The user selects one or more files to compress.
2. The user selects a destination folder for the output ZIP file.
3. When the "Compress" button is clicked:

   * A ZIP archive named `compressed.zip` is created in the selected destination.
   * All selected files are added to the archive (filename only, no directory structure).
4. A message "Compression completed!" is displayed when done.

## 🚀 How to Run

1. Make sure you have Python 3 installed.

2. Install the required GUI library if not already installed:

  ```bash
  pip install FreeSimpleGUI
  ````

3. Save the script and run it with Python:

   ```bash
   python files_zipper.py
   ```

## 📎 Example UI

```
+--------------------------------------------+
| Select files to compress:  [........][Choose] |
| Select destination:         [........][Choose] |
| [Compress]                                 |
| Compression completed!                     |
+--------------------------------------------+
```

## ⚠️ Known Issues

* The script attempts to compress files immediately after reading window values — it will try even if inputs are empty or incorrect. Consider adding input validation and handling the window's close event.

## ✅ Suggested Improvements that can be made:
  * Input validation (check for missing files or folders).
  * Custom filename for the ZIP archive.
  * Progress bar for large compressions.

