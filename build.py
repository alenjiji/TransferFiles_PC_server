import os
import shutil

def clean_build():
    """Clean previous build files"""
    dirs_to_clean = ['build', 'dist', 'release']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)

def build_app():
    """Build the application"""
    clean_build()
    os.system('pyinstaller --clean server.spec')
    
    # Create release folder
    if not os.path.exists('release'):
        os.makedirs('release')
    
    # Copy executable to release folder
    if os.path.exists('dist/FileTransferServer.exe'):
        os.makedirs('release/FileTransferServer', exist_ok=True)
        shutil.copy2('dist/FileTransferServer.exe', 'release/FileTransferServer')
        print("Build complete! Check the 'release/FileTransferServer' folder.")
    else:
        print("Build failed! Executable not found.")

if __name__ == '__main__':
    build_app()