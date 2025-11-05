import socket
import os

def connect_to_server(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    return client_socket

def send_file(client_socket, file_path):
    if os.path.isfile(file_path):
        client_socket.send(os.path.basename(file_path).encode())
        with open(file_path, 'rb') as file:
            data = file.read(1024)
            while data:
                client_socket.send(data)
                data = file.read(1024)
        print("File sent successfully.")
    else:
        print("File not found.")

def main():
    server_ip = "192.168.1.1"  # Replace with the server's IP address
    server_port = 5000          # Replace with the server's port number

    client_socket = connect_to_server(server_ip, server_port)
    
    file_path = input("Enter the path of the file to send: ")
    send_file(client_socket, file_path)
    
    client_socket.close()

if __name__ == "__main__":
    main()