import socket
import threading
import os
import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
from datetime import datetime
from flask import Flask, send_file, render_template_string, jsonify
import webbrowser

# Add Flask app
app = Flask(__name__)

class FileTransferServer:
    def __init__(self, window):
        self.window = window
        self.window.title("File Transfer Server")
        self.window.geometry("854x480")
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('Header.TLabel', font=('Segoe UI', 14, 'bold'))
        self.style.configure('Status.TLabel', font=('Segoe UI', 10))
        
        # Server settings
        self.SERVER_IP = '0.0.0.0'
        self.SERVER_PORT = 5001
        self.server_running = False
        self.shared_files = []

        self.setup_gui()
        self.get_local_ip()
        self.start_web_server()

    def setup_gui(self):
        # Main container
        main_container = ttk.Frame(self.window, padding="10")
        main_container.pack(fill='both', expand=True)

        # Header
        header_frame = ttk.Frame(main_container)
        header_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Label(header_frame, text="File Transfer Server", style='Header.TLabel').pack(side='left')
        
        # Status indicator
        self.status_label = ttk.Label(header_frame, text="Server Offline", style='Status.TLabel', foreground='red')
        self.status_label.pack(side='right')

        # Control panel
        control_frame = ttk.LabelFrame(main_container, text="Controls", padding="5")
        control_frame.pack(fill='x', pady=(0, 10))

        self.server_btn = ttk.Button(control_frame, text="Start Server", command=self.toggle_server, width=20)
        self.server_btn.pack(side='left', padx=5)

        ttk.Button(control_frame, text="Add Files", command=self.add_files, width=20).pack(side='left', padx=5)

        # IP display
        self.ip_label = ttk.Label(control_frame, text="", style='Status.TLabel')
        self.ip_label.pack(side='right', padx=5)

        # Main content area
        content_frame = ttk.Frame(main_container)
        content_frame.pack(fill='both', expand=True)
        
        # Files panel
        files_frame = ttk.LabelFrame(content_frame, text="Shared Files", padding="5")
        files_frame.pack(side='left', fill='both', expand=True, padx=(0, 5))

        # Add scrollbar to files list
        files_scroll = ttk.Scrollbar(files_frame)
        files_scroll.pack(side='right', fill='y')
        
        self.files_list = tk.Listbox(files_frame, yscrollcommand=files_scroll.set, 
                                    font=('Segoe UI', 10), activestyle='none')
        self.files_list.pack(fill='both', expand=True)
        files_scroll.config(command=self.files_list.yview)

        # Log panel
        log_frame = ttk.LabelFrame(content_frame, text="Server Log", padding="5")
        log_frame.pack(side='right', fill='both', expand=True)

        self.log_area = scrolledtext.ScrolledText(log_frame, font=('Consolas', 9))
        self.log_area.pack(fill='both', expand=True)

    def add_files(self):
        files = filedialog.askopenfilenames()
        for file in files:
            if file not in self.shared_files:
                self.shared_files.append(file)
                self.files_list.insert(tk.END, os.path.basename(file))
                self.log_message(f"Added file: {os.path.basename(file)}")

    def toggle_server(self):
        if not self.server_running:
            self.server_running = True
            self.server_btn.config(text="Stop Server")
            self.status_label.config(text="Server Online", foreground='green')
            self.ip_label.config(text=f"IP: {self.local_ip}:{self.SERVER_PORT}")
            server_thread = threading.Thread(target=self.start_server)
            server_thread.daemon = True
            server_thread.start()
        else:
            self.server_running = False
            self.server_btn.config(text="Start Server")
            self.status_label.config(text="Server Offline", foreground='red')
            self.ip_label.config(text="")
            self.server.close()
            self.log_message("Server stopped")

    def log_message(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_area.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_area.see(tk.END)
        self.log_area.tag_configure("timestamp", foreground="blue")
        self.log_area.tag_add("timestamp", f"end-2c linestart", f"end-2c linestart+10c")

    def handle_client(self, client_socket, addr):
        try:
            request = client_socket.recv(1024).decode('utf-8')
            filename = request.strip()

            # Find the full path of requested file
            full_path = None
            for shared_file in self.shared_files:
                if os.path.basename(shared_file) == filename:
                    full_path = shared_file
                    break

            if full_path and os.path.isfile(full_path):
                client_socket.send(b'EXISTS ' + str(os.path.getsize(full_path)).encode('utf-8'))
                with open(full_path, 'rb') as f:
                    bytes_to_send = f.read(1024)
                    while bytes_to_send:
                        client_socket.send(bytes_to_send)
                        bytes_to_send = f.read(1024)
                self.log_message(f"Sent {filename} to {addr[0]}")
            else:
                client_socket.send(b'NOT_FOUND')
                self.log_message(f"File not found: {filename}")
        except Exception as e:
            self.log_message(f"Error: {str(e)}")
        finally:
            client_socket.close()

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.SERVER_IP, self.SERVER_PORT))
        self.server.listen(5)
        self.log_message(f"Server started on {self.SERVER_IP}:{self.SERVER_PORT}")
        
        while self.server_running:
            try:
                client_socket, addr = self.server.accept()
                self.log_message(f"Connection from {addr[0]}")
                client_handler = threading.Thread(
                    target=self.handle_client, 
                    args=(client_socket, addr)
                )
                client_handler.daemon = True
                client_handler.start()
            except:
                break

    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 80))
            self.local_ip = s.getsockname()[0]
        except Exception:
            self.local_ip = '127.0.0.1'
        finally:
            s.close()

    def start_web_server(self):
        # Add web routes
        @app.route('/')
        def home():
            files = [os.path.basename(f) for f in self.shared_files]
            html = '''
            <!DOCTYPE html>
            <html>
            <head>
                <title>File Transfer</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    body { font-family: Arial; max-width: 800px; margin: 0 auto; padding: 20px; }
                    .file-list { list-style: none; padding: 0; }
                    .file-item { padding: 10px; margin: 5px 0; background: #f0f0f0; border-radius: 5px; }
                    .file-link { text-decoration: none; color: #333; display: block; }
                </style>
            </head>
            <body>
                <h2>Available Files</h2>
                <ul class="file-list">
                {% for file in files %}
                    <li class="file-item">
                        <a href="/download/{{ file }}" class="file-link">📁 {{ file }}</a>
                    </li>
                {% endfor %}
                </ul>
            </body>
            </html>
            '''
            return render_template_string(html, files=files)

        @app.route('/files')
        def files_json():
            files = [os.path.basename(f) for f in self.shared_files]
            return jsonify(files)

        @app.route('/download/<filename>')
        def download(filename):
            for shared_file in self.shared_files:
                if os.path.basename(shared_file) == filename:
                    return send_file(shared_file, as_attachment=True)
            return "File not found", 404

        # Start Flask in a separate thread
        flask_thread = threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000))
        flask_thread.daemon = True
        flask_thread.start()
        
        # Add web interface URL to log
        self.log_message(f"Web interface available at: http://{self.local_ip}:5000")

def main():
    root = tk.Tk()
    app = FileTransferServer(root)
    root.mainloop()

if __name__ == "__main__":
    main()