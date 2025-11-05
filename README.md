# File Transfer App

File Transfer App — lightweight PC server and Android client for sending files over a local hotspot.

This repository contains a simple Python-based PC server (tkinter GUI + Flask web UI) that shares selected files on your local network, and an Android client that can browse and download those files.

Project structure

- `src/server.py` — Main server script: tkinter GUI for sharing files and a small Flask web UI for mobile downloads.
- `src/client.py` — Optional CLI client (if present).
- `src/utils/` — Utility helpers (networking, file handling).
- `src/config/settings.py` — Configuration (server IP / port).
- `requirements.txt` — Python dependencies.
- `build.py`, `server.spec` — Optional packaging helpers (PyInstaller).

Quick setup

1. Clone the repository:

   git clone https://github.com/YOUR_USERNAME/TransferFiles_PC_server.git

2. Change to the project directory:

   cd file-transfer-app

3. Create a virtual environment (recommended) and install dependencies:

   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt

4. Run the server:

   python src\server.py

Usage

- Start the server on your PC. The GUI allows you to add files to share and start/stop the server.
- The server log will print a web UI URL (for example: http://192.168.1.100:5000). Open that URL on your Android device's browser to view and download files.
- Alternatively, use the companion Android client (if available) and point it at the server IP (http://<PC-IP>:5000) to fetch the file list and download.

Notes

- Ensure both PC and Android device are on the same Wi-Fi / hotspot network.
- Allow the server ports (default 5000 for web UI) through Windows Firewall if needed.
- The `.venv` directory is ignored by `.gitignore`; do not commit virtual environments.

License & contribution

- Add a LICENSE file or contribution guidelines if you plan to share the repo publicly.

If you want, I can also create a compact `README.md` with examples and screenshots or produce a release-ready packaging script.
<<<<<<< HEAD
# TransferFiles_PC_server
File Transfer App — lightweight PC server and Android client for sending files over a local hotspot. Run the PC server (tkinter GUI + Flask web UI) to share selected files; open the server URL on an Android device or use the Android app to browse and download files.
=======
# Contents of `README.md`

# File Transfer App

This project allows users to transfer files from a PC to Android devices through a hotspot connection.

## Project Structure

- `src/server.py`: Main server script that listens for incoming connections from Android devices and handles file transfers.
- `src/client.py`: Client script that runs on the Android device, connecting to the server and sending file requests.
- `src/utils/`: Contains utility functions for network management and file handling.
  - `__init__.py`: Initializes the utils package.
  - `network.py`: Functions for managing network connections.
  - `file_handler.py`: Functions for handling file operations during transfers.
- `src/config/settings.py`: Configuration settings for the application, including server IP address and port number.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Setup Instructions

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
4. Run the server script on your PC:
   ```
   python src/server.py
   ```
5. Run the client script on your Android device to connect to the server and initiate file transfers.

## Usage Guidelines

- Ensure both the PC and Android device are connected to the same hotspot.
- Configure the server settings in `src/config/settings.py` as needed.
- Follow the prompts in the client application to select files for transfer.
>>>>>>> 72351d0 (Initial commit: file transfer server (tkinter + Flask web UI))
