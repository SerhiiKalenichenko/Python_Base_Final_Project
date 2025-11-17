Personal Assistant - Complete Installation Guide
================================================

System Requirements
-------------------
- Operating System: Windows 7/10/11, Mac OS X 10.9+, or Linux
- Python Version: 3.7 or newer
- Disk Space: 100MB free space

Step 1: Install Python
----------------------

1. Download Python:
   - Open your web browser and go to: https://python.org/downloads/
   - Click the large yellow "Download Python" button

2. Install Python:

   For Windows:
   - Run the downloaded .exe file
   - IMPORTANT: Check the box "Add Python to PATH"
   - Click "Install Now"
   - Wait for installation to complete

   For Mac:
   - Run the downloaded .pkg file
   - Follow the installation wizard steps
   - Python will be installed automatically

   For Linux:
   - Python is usually pre-installed
   - To verify, open Terminal and type: python3 --version
   - If not installed, use your distribution's package manager

Step 2: Download the Project
----------------------------

1. Download the project ZIP file from the provided source
2. Extract the ZIP file to a location of your choice:

   Windows:
   - Right-click the ZIP file
   - Select "Extract All..."
   - Choose destination folder (e.g., Desktop, Documents)

   Mac:
   - Double-click the ZIP file
   - It will automatically extract to the same location

   Linux:
   - Right-click the ZIP file and select "Extract Here"
   - Or use command: unzip filename.zip

Step 3: Install the Program
---------------------------

1. Open Terminal/Command Prompt in the project folder:

   Windows:
   - Navigate to the extracted project folder
   - Hold Shift and right-click in an empty area of the folder
   - Select "Open PowerShell window here" or "Open command window here"

   Mac:
   - Navigate to the extracted project folder
   - Right-click the folder and select "New Terminal at Folder"

   Linux:
   - Navigate to the extracted project folder
   - Right-click the folder and select "Open in Terminal"

2. Run the installation command:

   For Windows:
   py -m pip install -e .

   For Mac/Linux:
   python3 -m pip install -e .

   This command will:
   - Install the Personal Assistant as a Python package
   - Automatically install all required dependencies
   - Make the program accessible from anywhere on your system

Step 4: Run the Program
-----------------------

After successful installation, you can run the program using:

Method 1: Using the installed command (recommended):
call-assistant

Method 2: Direct execution from project folder:
   
   Windows:
   python main.py
   or
   py main.py

   Mac/Linux:
   python3 main.py

Verification
------------
If the installation was successful, you should see the Personal Assistant interface.

Troubleshooting
---------------

Problem: "Python not found" or "pip not found"
Solution:
- Reinstall Python, making sure to check "Add Python to PATH" (Windows)
- Use python -m pip instead of just pip
- Try python3 instead of python (Mac/Linux)

Problem: "call-assistant command not found"
Solution:
- Run the program directly using python main.py from the project folder
- Try the command personal-assistant

Problem: Program opens and closes immediately
Solution:
- Open terminal in the project folder
- Run python main.py to see error messages

Problem: Permission errors (Mac/Linux)
Solution:
- Try: sudo python3 -m pip install -e .

Problem: Dependencies not installing properly
Solution:
- Manually install key dependencies:
  pip install colorama rich prompt-toolkit Pygments

Getting Help
------------
If you continue to experience problems:

1. Take a screenshot of any error messages
2. Verify Python installation by running: python --version
3. Ensure all project files are in the correct folder structure
4. Check that you're running commands from the correct project folder

Uninstallation
--------------
To remove the program:
   For Windows:
   py -m pip uninstall personal-assistant

   For Mac/Linux:
   pip uninstall personal-assistant

Additional Notes
----------------
- This program has been tested on Windows and should work on Mac/Linux
- The installation process automatically handles all dependencies
- No advanced technical knowledge is required to install and use this program

For further assistance, please contact our development team.
