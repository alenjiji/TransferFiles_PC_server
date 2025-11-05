Write-Host "Installing File Transfer Server Dependencies..." -ForegroundColor Green

# Check if Python is installed
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Host "Python is not installed. Please install Python 3.x from https://www.python.org/downloads/" -ForegroundColor Red
    Write-Host "Press any key to exit..."
    $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
    exit 1
}

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Cyan
python -m venv .venv

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Cyan
.\.venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Cyan
python -m pip install --upgrade pip
pip install Flask==3.1.2 Werkzeug>=3.0.0 tk

Write-Host "`nInstallation complete!" -ForegroundColor Green
Write-Host "You can now run FileTransferServer.exe" -ForegroundColor Green
Write-Host "`nPress any key to exit..."
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')