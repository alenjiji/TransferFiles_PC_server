# setup.ps1

Param (
    [switch]$Clean = $false
)

Write-Host "=== TransferFiles_PC_server Setup ==="

# 1. Optionally clean previous build (if desired)
if ($Clean) {
    Write-Host "Cleaning previous build artifacts..."
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue ".\dist"
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue ".\build"
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue ".\*.spec"
}

# 2. Ensure Python is installed
Write-Host "Checking Python installation..."
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Error "Python is not found. Please install Python 3.x and try again."
    exit 1
}

# 3. Create/Activate virtual environment (optional)
$venvPath = ".\venv"
if (-not (Test-Path $venvPath)) {
    Write-Host "Creating virtual environment..."
    python -m venv $venvPath
}
Write-Host "Activating virtual environment..."
& "$venvPath\Scripts\Activate.ps1"

# 4. Install dependencies from requirements.txt
Write-Host "Installing Python dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r .\requirements.txt

# 5. Build the application (executable) using build.py
Write-Host "Building the application..."
python .\build.py

# 6. Locate the executable (assumes build output places an exe in 'dist' folder)
$exePath = Get-ChildItem -Path .\dist -Filter *.exe -Recurse | Select-Object -First 1
if (-not $exePath) {
    Write-Error "Executable not found in 'dist' folder. Build may have failed."
    exit 1
}

Write-Host "Executable found at: $($exePath.FullName)"

# 7. Optionally install the release (could be copying to Program Files, creating shortcut, etc.)
# Here is a simple example: copy exe to a folder and optionally create a shortcut on Desktop.
$installFolder = "$env:ProgramFiles\TransferFiles_PC_server"
if (-not (Test-Path $installFolder)) {
    Write-Host "Creating install folder: $installFolder"
    New-Item -ItemType Directory -Force -Path $installFolder
}
Write-Host "Installing application..."
Copy-Item -Path $exePath.FullName -Destination $installFolder -Force

# Create desktop shortcut
$desktop = [Environment]::GetFolderPath("Desktop")
$lnkPath = Join-Path $desktop "TransferFiles_PC_server.lnk"
$targetPath = Join-Path $installFolder $exePath.Name

Write-Host "Creating desktop shortcut..."
$WshShell = New-Object -ComObject WScript.Shell
$shortcut = $WshShell.CreateShortcut($lnkPath)
$shortcut.TargetPath = $targetPath
$shortcut.WorkingDirectory = $installFolder
$shortcut.WindowStyle = 1
$shortcut.Save()

Log "============================================================"
Log " All installations completed successfully!"
Log "============================================================"
Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1