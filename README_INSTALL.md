# File Transfer Server Installation Guide

## Prerequisites
- Windows operating system
- Python 3.x installed (Download from https://www.python.org/downloads/)
- PowerShell (comes pre-installed with Windows)

## Installation Steps

1. Extract all files from the downloaded package to a folder
2. Right-click on `setup.ps1` and select "Run with PowerShell"
   - If you get a security warning, you may need to run:
     ```powershell
     Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
     ```
   - Then run `.\setup.ps1`
3. Wait for the installation to complete
4. Run `FileTransferServer.exe` to start the application

## Manual Installation (if setup.ps1 fails)

If you encounter any issues with the automatic setup, you can install manually:

1. Open Command Prompt or PowerShell
2. Navigate to the application folder
3. Create a virtual environment:
   ```
   python -m venv .venv
   ```
4. Activate the virtual environment:
   ```
   .\.venv\Scripts\activate
   ```
5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Run `FileTransferServer.exe`

## Troubleshooting

- If you get "Python is not installed" error, make sure to install Python 3.x from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during Python installation
- If you get permission errors, try running PowerShell as Administrator