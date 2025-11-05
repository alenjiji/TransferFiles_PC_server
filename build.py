import os
import shutil
import sys
import subprocess


def clean_build():
    """Clean previous build files"""
    dirs_to_clean = ["build", "dist", "release"]
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)


def run_pyinstaller(spec_file="server.spec"):
    """Run PyInstaller using the current Python interpreter (avoids relying on PATH).

    Returns True on success, False otherwise.
    """
    cmd = [sys.executable, "-m", "PyInstaller", "--clean", spec_file]
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print("PyInstaller failed with exit code:", e.returncode)
        return False
    except FileNotFoundError:
        # This happens when the python executable can't run the module; give actionable hint
        print("PyInstaller module not found. Install it with:")
        print(f"  {sys.executable} -m pip install pyinstaller")
        return False


def find_executable():
    """Try to locate the generated executable in common dist locations."""
    candidates = [
        os.path.join("dist", "FileTransferServer.exe"),
        os.path.join("dist", "FileTransferServer", "FileTransferServer.exe"),
    ]
    for p in candidates:
        if os.path.exists(p):
            return p
    # fallback: try to find any .exe directly under dist
    if os.path.isdir("dist"):
        for root, dirs, files in os.walk("dist"):
            for f in files:
                if f.lower().endswith(".exe"):
                    return os.path.join(root, f)
    return None


def build_app():
    """Build the application"""
    clean_build()

    print("Running PyInstaller (this may take a while)...")
    ok = run_pyinstaller("server.spec")
    if not ok:
        print("Build failed because PyInstaller did not complete successfully.")
        return

    exe_path = find_executable()

    # Create release folder
    if not os.path.exists("release"):
        os.makedirs("release")

    if exe_path:
        target_dir = os.path.join("release", os.path.splitext(os.path.basename(exe_path))[0])
        os.makedirs(target_dir, exist_ok=True)
        shutil.copy2(exe_path, target_dir)
        print("Build complete! Check the release folder:", target_dir)
    else:
        print("Build finished but no executable was found in 'dist/'. Check PyInstaller output for errors.")


if __name__ == "__main__":
    build_app()