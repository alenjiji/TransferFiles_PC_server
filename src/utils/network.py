import socket

def create_server_socket(host='0.0.0.0', port=5000):
    """Create a server socket to listen for incoming connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    return server_socket

def accept_client_connection(server_socket):
    """Accept a client connection."""
    client_socket, addr = server_socket.accept()
    print(f"Connection accepted from {addr}")
    return client_socket

def close_connection(sock):
    """Close the given socket connection."""
    sock.close()
    print("Connection closed.")