import socket
import threading
from cryptography.fernet import Fernet
import ssl
import os

# Load or generate the encryption key
key_file_path = "encryption_key.txt"
if os.path.exists(key_file_path):
    with open(key_file_path, "rb") as key_file:
        key = key_file.read()
else:
    key = Fernet.generate_key()
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)
cipher_suite = Fernet(key)

# Function to handle client connections
def handle_client(client_socket):
    encrypted_message = client_socket.recv(1024)
    message = cipher_suite.decrypt(encrypted_message).decode("utf-8")
    print(f"Received encrypted message: {encrypted_message}")
    print(f"Decrypted message: {message}")
    client_socket.close()

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 0))  # Bind to any available port
server_socket.listen()

# Wrap the socket with SSL for HTTPS
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")
ssl_socket = context.wrap_socket(server_socket, server_side=True)

# Get the server's IP address and port
server_ip = socket.gethostbyname(socket.gethostname())
server_port = ssl_socket.getsockname()[1]

# Generate the link
link = f"https://{server_ip}:{server_port}"
print(f"Link for secure communication: {link}")
print("The Unknow by Trapzzy")

# Server main loop
try:
    while True:
        client_socket, address = ssl_socket.accept()
        print(f"Connection from {address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
finally:
    ssl_socket.close()
    server_socket.close()
