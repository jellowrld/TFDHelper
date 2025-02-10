# TFDHelper
Helper for TFD for use in combination with Hacks.
Inflitration requires Auto Press (3rd ability  and Bunny) to funcction properly.. might still work with others?

![Menu Screenshot](https://github.com/user-attachments/assets/0fc02944-e853-476d-9987-61ee00db7689)


To run the code, follow this detailed step-by-step guide:

### 1. **Python (Version 3.6 or later)**
Make sure that Python is installed on your computer. You can check if Python is installed by running the following command in your terminal or command prompt:

```bash
python --version
```

If Python is not installed:
- Download and install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

### 2. **Required Libraries**
You will need several Python libraries for the script to function correctly. Install them using `pip`.

- **Tkinter** (for GUI):
  - Tkinter is bundled with Python, so you shouldn’t need to install it separately. If you are missing it:
    - On **Windows**, Tkinter is included by default.
    - On **macOS**, Tkinter should already be available.
    - On **Linux** (Ubuntu/Debian-based systems), install it using:
      ```bash
      sudo apt-get install python3-tk
      ```

- **keyboard** (for listening to keyboard events):
  - Install using pip:
    ```bash
    pip install keyboard
    ```

- **Pillow** (for image processing and screen capturing):
  - Install using pip:
    ```bash
    pip install pillow
    ```

- **pytesseract** (for Optical Character Recognition, OCR):
  - Install using pip:
    ```bash
    pip install pytesseract
    ```
  - You also need to install **Tesseract OCR** itself, which the `pytesseract` library uses:
    - **Windows**:
      - Download the Tesseract installer from [Tesseract-UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) (for Windows).
      - Install Tesseract and make sure to add it to your system’s **PATH** during installation.
    - **macOS**:
      - Install via Homebrew:
        ```bash
        brew install tesseract
        ```
    - **Linux (Ubuntu/Debian-based systems)**:
      ```bash
      sudo apt-get install tesseract-ocr
      ```

- **pyautogui** (for automating mouse and keyboard actions):
  - Install using pip:
    ```bash
    pip install pyautogui
    ```

### 3. **Operating System**
The script is designed to run on **Windows**, **macOS**, or **Linux**, but the screen resolution and window positioning are hardcoded for a **1920x1080** screen. You will need to adjust the window size or code if your screen resolution is different.

### 4. **Permissions**
- Some libraries, such as `keyboard`, may require elevated permissions (administrator rights) to detect key presses. So, you might need to run the script with administrative privileges depending on your operating system.

### 5. **Tesseract OCR Language Packs (Optional)**
If you want to recognize text in languages other than English, you may need additional language packs for Tesseract. You can download these from the [Tesseract GitHub page](https://github.com/tesseract-ocr/tesseract) or from the official Tesseract website.

### 6. **Save the Script**
- Save the provided Python script to a file (e.g., `helper.py`).

### 7. **Running the Code**
Once you've installed all the required libraries and ensured that Tesseract is installed correctly, you can run the script by following these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the script (`helper.py`) is saved.
3. Run the Python script using the following command:

   ```bash
   python helper.py
   ```

### 8. **Using the Script**
- Once the script is running, you can interact with it using the GUI that appears on your screen. The GUI allows you to toggle different automation tasks by pressing hotkeys (`F12`, `F10`, `F9`, etc.).
- The GUI will display the current status of each task (e.g., `Colossi Restart`, `Restart Field Mission`, and `Infiltration Operation Bot`).

### 9. **Troubleshooting**

- **Tesseract Not Found:** Ensure that you’ve installed Tesseract and that it's correctly added to your system's PATH. Verify it by running the command `tesseract --version` in the terminal.
  
- **Missing Libraries:** Ensure you’ve installed all the required libraries using `pip install ...`.

- **Permissions Issues:** The `keyboard` library may require administrator permissions on some operating systems to work properly. Make sure to run the script with elevated privileges if necessary.

- **Adjusting for Different Screen Resolutions:** The script assumes a screen resolution of 1920x1080. If your screen resolution is different, you may need to adjust the screen coordinates defined in the script (e.g., `(1623, 536, 1770, 566)`).

- Also please note that the release should include everything needed to run so you shoould be able to bypass all this setup using the EXE release.
