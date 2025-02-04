# TFDHelper
Helper for TFD for use in combination with Hacks.
![Menu Screenshot](https://github.com/user-attachments/assets/0fc02944-e853-476d-9987-61ee00db7689)


To run the code, you'll need to ensure that the following libraries and tools are installed on your system:

### 1. **Python** (Version 3.6 or later)
   - Make sure Python is installed on your computer. You can check if Python is installed by running `python --version` in your terminal or command prompt.

### 2. **Required Libraries**
   - You will need to install several Python libraries to run the script successfully. Here's a list of them:
   
   - **Tkinter** (for GUI)
     - Tkinter is typically bundled with Python, so you shouldn't need to install it separately. If it's not available, you can install it using the following:
       - On Windows, Tkinter should already be included.
       - On Linux, you can install it using:
         ```bash
         sudo apt-get install python3-tk
         ```
       - On macOS, Tkinter should be available by default.

   - **keyboard** (to listen to keyboard events)
     - Install this library via pip:
       ```bash
       pip install keyboard
       ```

   - **Pillow** (for image processing and screen capturing)
     - Install this library via pip:
       ```bash
       pip install pillow
       ```

   - **pytesseract** (for Optical Character Recognition, OCR)
     - Install this library via pip:
       ```bash
       pip install pytesseract
       ```
     - Additionally, you'll need to install Tesseract itself, which is the OCR engine used by `pytesseract`. Here's how to install it:

       **Windows:**
       - Download the Tesseract installer from: https://github.com/UB-Mannheim/tesseract/wiki
       - Install Tesseract and add it to your system’s PATH environment variable.

       **macOS:**
       ```bash
       brew install tesseract
       ```

       **Linux (Ubuntu/Debian-based systems):**
       ```bash
       sudo apt-get install tesseract-ocr
       ```

   - **pyautogui** (for automating mouse and keyboard actions)
     - Install this library via pip:
       ```bash
       pip install pyautogui
       ```

### 3. **Operating System**
   - The script is written for use with Windows, macOS, or Linux. However, screen resolution and window positioning are hardcoded for a 1920x1080 screen, so make sure to adjust the window size or the code if your screen is of a different resolution.

### 4. **Additional Notes:**
   - **Permissions:** Some of the libraries (such as `keyboard`) may require elevated permissions (administrator rights) to detect key presses, so make sure to run the script with the necessary permissions.
   - **Keyboard Hooks:** The `keyboard` library uses system-level hooks to detect keys, so it may require running with administrative privileges depending on your operating system.
   - **Tesseract OCR Language Packs:** If you plan on recognizing text in languages other than English, you may need to install additional language packs for Tesseract. You can do this by downloading the language files from Tesseract's GitHub page or its official website.

### Running the Code:
1. Install all the required libraries as mentioned above.
2. Make sure Tesseract is installed and added to the system's PATH.
3. Save the script to a `.py` file.
4. Run the Python script using the following command:
   ```bash
   python helper.py
   ```
