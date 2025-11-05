# File Transfer App

File Transfer App — lightweight PC server and Android client for sending files over a local hotspot.

This repository contains a simple Python-based PC server (tkinter GUI + Flask web UI) that shares selected files on your local network, and an Android client that can browse and download those files.

## Quick Installation (Pre-built Executable)

1. Download the latest release from the [Releases page](https://github.com/alenjiji/TransferFiles_PC_server/releases)
2. Extract all files to a folder of your choice
3. Run the installation script:
   - Right-click on `setup.ps1` and select "Run with PowerShell"
   - If you get a security warning, run this command in PowerShell:
     ```powershell
     Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force; .\setup.ps1
     ```
4. Once setup is complete, double-click `FileTransferServer.exe` to start the application

For detailed installation instructions and troubleshooting, see [README_INSTALL.md](README_INSTALL.md).

## Usage

1. Start `FileTransferServer.exe` on your PC
2. Use the GUI to:
   - Add files you want to share
   - Start/stop the server
   - View server status and IP address
3. On your Android device:
   - Connect to the same Wi-Fi network as the PC
   - Open the displayed URL (e.g., http://192.168.1.100:5000) in your browser
4. Browse and download shared files

## Development Setup

If you want to run from source or contribute to development:

1. Clone the repository:

   git clone https://github.com/alenjiji/TransferFiles_PC_server.git

2. Change to the project directory:

   cd file-transfer-app

3. Create a virtual environment (recommended) and install dependencies:

   python -m venv .venv
   .\\.venv\\Scripts\\activate
   pip install -r requirements.txt

4. Run the server:
   ```bash
   python src\server.py
   ```

## Project Structure

- `src/server.py` — Main server script with GUI and web interface
- `src/client.py` — Optional CLI client
- `src/utils/` — Utility helpers (networking, file handling)
- `src/config/settings.py` — Configuration (server IP / port)
- `requirements.txt` — Python dependencies
- `build.py`, `server.spec` — Packaging scripts (PyInstaller)
- `setup.ps1` — Installation script for Windows
- `README_INSTALL.md` — Detailed installation guide

## Notes

- Ensure both PC and Android device are on the same Wi-Fi / hotspot network
- Allow the server through Windows Firewall if needed (default port: 5000)
- The application works best with modern browsers and Python 3.x

## License & Contributing

This project is open source. Feel free to contribute by:
- Reporting issues
- Suggesting new features
- Submitting pull requests

## Troubleshooting

If you encounter any issues:
1. Check the [README_INSTALL.md](README_INSTALL.md) for common solutions
2. Make sure your firewall allows the application
3. Verify both devices are on the same network
4. Check if Python is properly installed (if running from source)
